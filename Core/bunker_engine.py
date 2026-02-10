# ============================================================
# bunker_engine.py
# NEXO / ZYRA — MOTOR DE SEGURIDAD & IDENTIDAD (SUPER BÚNKER)
# Nivel Silicon Valley | Jerarquía L1-L4 | Inmutable
# ============================================================

import os
import json
import uuid
from datetime import datetime

# Conexión al Cerebro Central (Ledger)
try:
    from zyra_ledger_hook import ledger_record
except ImportError:
    def ledger_record(*args, **kwargs): print(f"[MOCK SECURITY] {kwargs}")

# -----------------------------
# CONFIGURACIÓN DE RUTAS
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "security")
os.makedirs(DATA_DIR, exist_ok=True)

IDENTITIES_FILE = os.path.join(DATA_DIR, "identities_db.json")
ACCESS_LOG_FILE = os.path.join(DATA_DIR, "access_log.json")

# -----------------------------
# NIVELES DE SEGURIDAD & BLOQUEO (LA JERARQUÍA)
# -----------------------------
class SecurityLevel:
    PUBLIC = 0
    CLIENT = 1    # Usuario Final
    STAFF = 2     # Empleado
    MANAGER = 3   # Gerente (Puede desbloquear L1/L2)
    ROOT = 4      # Dueño / JAZA (Puede desbloquear TODO)

class LockLevel:
    NONE = 0
    L1_SOFT = 1   # Bloqueo por contraseña (Autoservicio)
    L2_HARD = 2   # Bloqueo por comportamiento (Requiere Manager)
    L3_CRIT = 3   # Bloqueo por riesgo financiero (Requiere Root)
    L4_NUKE = 4   # Amenaza de Intrusión (Sellado Total)

# -----------------------------
# UTILIDADES DE PERSISTENCIA
# -----------------------------
def _now(): return datetime.utcnow().isoformat()

def _load(path):
    if not os.path.exists(path): return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except: return []

def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# -----------------------------
# GESTIÓN DE IDENTIDAD (ALTA DE USUARIOS)
# -----------------------------
def register_identity(full_name, role_name, created_by_id):
    """
    Crea una identidad digital en el Búnker.
    """
    # Asignación automática de nivel basada en el rol
    level = SecurityLevel.CLIENT
    if role_name in ["ROOT", "DUEÑO"]: level = SecurityLevel.ROOT
    elif role_name in ["MANAGER", "GERENTE"]: level = SecurityLevel.MANAGER
    elif role_name in ["VENDEDOR", "CONTADOR"]: level = SecurityLevel.STAFF

    new_id = str(uuid.uuid4())
    
    identity = {
        "id": new_id,
        "full_name": full_name,
        "role": role_name,
        "security_level": level,
        "lock_level": LockLevel.NONE,  # Empieza desbloqueado
        "failed_attempts": 0,
        "biometric_hash": "PENDING",   # Placeholder para huella/faceID
        "created_at": _now(),
        "created_by": created_by_id
    }

    identities = _load(IDENTITIES_FILE)
    identities.append(identity)
    _save(IDENTITIES_FILE, identities)

    ledger_record("IDENTITY_CREATED", "OK", {"id": new_id, "rol": role_name}, "BUNKER")
    return identity

def get_identity(identity_id):
    identities = _load(IDENTITIES_FILE)
    for i in identities:
        if i["id"] == identity_id: return i
    return None

def _update_identity(identity_data):
    identities = _load(IDENTITIES_FILE)
    for idx, i in enumerate(identities):
        if i["id"] == identity_data["id"]:
            identities[idx] = identity_data
            _save(IDENTITIES_FILE, identities)
            return True
    return False

# -----------------------------
# LÓGICA DE DEFENSA ACTIVA (EL ESCUDO)
# -----------------------------
def report_security_incident(identity_id, incident_type):
    """
    El cerebro del Búnker. Decide qué nivel de bloqueo aplicar
    según la gravedad del incidente.
    """
    identity = get_identity(identity_id)
    if not identity: return {"error": "Usuario desconocido"}

    lock_applied = LockLevel.NONE
    msg = ""

    # CASO 1: Error de dedo (Contraseña mal)
    if incident_type == "LOGIN_FAIL":
        identity["failed_attempts"] += 1
        if identity["failed_attempts"] >= 3:
            identity["lock_level"] = LockLevel.L1_SOFT
            lock_applied = LockLevel.L1_SOFT
            msg = "Bloqueo L1 (Intentos fallidos). Requiere reseteo."

    # CASO 2: Comportamiento Raro (IP extraña, horario inusual)
    elif incident_type == "SUSPICIOUS_BEHAVIOR":
        identity["lock_level"] = LockLevel.L2_HARD
        lock_applied = LockLevel.L2_HARD
        msg = "Bloqueo L2 (Comportamiento). Requiere Manager."

    # CASO 3: Riesgo Financiero (Intentar mover millones sin permiso)
    elif incident_type == "RISK_FINANCE":
        identity["lock_level"] = LockLevel.L3_CRIT
        lock_applied = LockLevel.L3_CRIT
        msg = "Bloqueo L3 (Riesgo). Requiere Dueño/Root."

    # CASO 4: HACKING / INTRUSIÓN (Nuclear)
    elif incident_type == "INTRUSION_DETECTED":
        identity["lock_level"] = LockLevel.L4_NUKE
        lock_applied = LockLevel.L4_NUKE
        msg = "🚫 BLOQUEO L4 (AMENAZA ACTIVA). CUENTA CONGELADA."

    _update_identity(identity)

    # Si hubo bloqueo, lo gritamos al Ledger Central
    if lock_applied > 0:
        ledger_record("SECURITY_LOCK", f"LEVEL_{lock_applied}", 
                     {"target": identity["full_name"], "reason": incident_type}, "BUNKER_AI")
        print(f"🔒 [BUNKER] {msg}")
    
    return {"current_lock": identity["lock_level"], "attempts": identity["failed_attempts"]}

# -----------------------------
# SISTEMA DE DESBLOQUEO JERÁRQUICO
# -----------------------------
def execute_unlock(target_id, authorizer_id, method="MANUAL"):
    """
    Verifica si el 'authorizer' tiene rango suficiente para quitar
    el bloqueo del 'target'.
    """
    target = get_identity(target_id)
    admin = get_identity(authorizer_id)

    if not target or not admin: return False

    current_lock = target["lock_level"]
    admin_rank = admin["security_level"]

    # REGLAS DE ORO DEL BÚNKER (Jerarquía)
    authorized = False

    if current_lock == LockLevel.NONE:
        return True # Ya estaba desbloqueado

    elif current_lock == LockLevel.L1_SOFT:
        # Cualquiera puede desbloquear L1 con su propio correo (simulado aqui con manager)
        if admin_rank >= SecurityLevel.STAFF: authorized = True

    elif current_lock == LockLevel.L2_HARD:
        # Solo Manager o superior
        if admin_rank >= SecurityLevel.MANAGER: authorized = True
    
    elif current_lock == LockLevel.L3_CRIT:
        # Solo ROOT/Dueño
        if admin_rank >= SecurityLevel.ROOT: authorized = True

    elif current_lock == LockLevel.L4_NUKE:
        # L4 es especial. Incluso ROOT necesita doble validación (Simulado)
        if admin_rank == SecurityLevel.ROOT: authorized = True
    
    if authorized:
        target["lock_level"] = LockLevel.NONE
        target["failed_attempts"] = 0
        _update_identity(target)
        ledger_record("SECURITY_UNLOCK", "SUCCESS", 
                     {"target": target["full_name"], "admin": admin["full_name"]}, "BUNKER_ADMIN")
        print(f"✅ [BUNKER] Usuario {target['full_name']} DESBLOQUEADO por {admin['full_name']}")
        return True
    else:
        print(f"⛔ [ACCESO DENEGADO] {admin['full_name']} (Nivel {admin_rank}) no tiene rango para quitar Bloqueo L{current_lock}.")
        ledger_record("UNLOCK_FAIL", "FORBIDDEN", 
                     {"target": target_id, "admin": authorizer_id}, "BUNKER_SECURITY")
        return False

# -----------------------------
# PRUEBA DE FUEGO (EJECUCIÓN)
# -----------------------------
if __name__ == "__main__":
    print("--- 🛡️ INICIANDO SUPER BÚNKER ZYRA ---")

    # 1. Crear Jerarquía
    root = register_identity("Jose Zelaya (CEO)", "ROOT", "SYSTEM")
    manager = register_identity("Gerente Operaciones", "MANAGER", root["id"])
    vendedor = register_identity("Vendedor Junior", "VENDEDOR", manager["id"])

    uid = vendedor["id"]
    
    # 2. ESCENARIO: Ataque de Intrusión (L4)
    print("\n--- SIMULANDO ATAQUE DE HACKER ---")
    report_security_incident(uid, "INTRUSION_DETECTED") # Bloqueo L4 inmediato

    # 3. ESCENARIO: Gerente intenta desbloquear (Debería fallar)
    print("\n--- INTENTO DE RESCATE POR GERENTE ---")
    execute_unlock(uid, manager["id"])

    # 4. ESCENARIO: CEO (Root) intenta desbloquear (Debería funcionar)
    print("\n--- INTENTO DE RESCATE POR CEO (ROOT) ---")
    execute_unlock(uid, root["id"])
