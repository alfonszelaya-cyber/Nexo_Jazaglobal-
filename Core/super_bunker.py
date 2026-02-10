# ============================================================
# super_bunker.py
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
    except: 
        return []

def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# -----------------------------
# CLASE PRINCIPAL (INYECCIÓN CORE)
# -----------------------------
class SUPER_BUNKER:
    def __init__(self):
        self.engine_name = "SUPER_BUNKER"
        self.version = "1.0.0"

    # -----------------------------
    # GESTIÓN DE IDENTIDAD
    # -----------------------------
    def register_identity(self, full_name, role_name, created_by_id):
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
            "lock_level": LockLevel.NONE,
            "failed_attempts": 0,
            "biometric_hash": "PENDING",
            "created_at": _now(),
            "created_by": created_by_id
        }

        identities = _load(IDENTITIES_FILE)
        identities.append(identity)
        _save(IDENTITIES_FILE, identities)

        ledger_record("IDENTITY_CREATED", "OK", {"id": new_id, "rol": role_name}, "BUNKER")
        return identity

    def get_identity(self, identity_id):
        identities = _load(IDENTITIES_FILE)
        for i in identities:
            if i["id"] == identity_id: 
                return i
        return None

    def _update_identity(self, identity_data):
        identities = _load(IDENTITIES_FILE)
        for idx, i in enumerate(identities):
            if i["id"] == identity_data["id"]:
                identities[idx] = identity_data
                _save(IDENTITIES_FILE, identities)
                return True
        return False

    # -----------------------------
    # DEFENSA ACTIVA
    # -----------------------------
    def report_security_incident(self, identity_id, incident_type):
        identity = self.get_identity(identity_id)
        if not identity: 
            return {"error": "Usuario desconocido"}

        lock_applied = LockLevel.NONE
        msg = ""

        if incident_type == "LOGIN_FAIL":
            identity["failed_attempts"] += 1
            if identity["failed_attempts"] >= 3:
                identity["lock_level"] = LockLevel.L1_SOFT
                lock_applied = LockLevel.L1_SOFT
                msg = "Bloqueo L1 (Intentos fallidos)."

        elif incident_type == "SUSPICIOUS_BEHAVIOR":
            identity["lock_level"] = LockLevel.L2_HARD
            lock_applied = LockLevel.L2_HARD
            msg = "Bloqueo L2 (Comportamiento)."

        elif incident_type == "RISK_FINANCE":
            identity["lock_level"] = LockLevel.L3_CRIT
            lock_applied = LockLevel.L3_CRIT
            msg = "Bloqueo L3 (Riesgo)."

        elif incident_type == "INTRUSION_DETECTED":
            identity["lock_level"] = LockLevel.L4_NUKE
            lock_applied = LockLevel.L4_NUKE
            msg = "🚫 BLOQUEO L4 (INTRUSIÓN)."

        self._update_identity(identity)

        if lock_applied > 0:
            ledger_record("SECURITY_LOCK", f"LEVEL_{lock_applied}", 
                         {"target": identity["full_name"], "reason": incident_type}, "BUNKER_AI")
            print(f"🔒 [BUNKER] {msg}")
        
        return {"current_lock": identity["lock_level"], "attempts": identity["failed_attempts"]}

    # -----------------------------
    # DESBLOQUEO JERÁRQUICO
    # -----------------------------
    def execute_unlock(self, target_id, authorizer_id, method="MANUAL"):
        target = self.get_identity(target_id)
        admin = self.get_identity(authorizer_id)

        if not target or not admin: 
            return False

        current_lock = target["lock_level"]
        admin_rank = admin["security_level"]
        authorized = False

        if current_lock == LockLevel.NONE:
            return True

        elif current_lock == LockLevel.L1_SOFT:
            if admin_rank >= SecurityLevel.STAFF: authorized = True

        elif current_lock == LockLevel.L2_HARD:
            if admin_rank >= SecurityLevel.MANAGER: authorized = True
        
        elif current_lock == LockLevel.L3_CRIT:
            if admin_rank >= SecurityLevel.ROOT: authorized = True

        elif current_lock == LockLevel.L4_NUKE:
            if admin_rank == SecurityLevel.ROOT: authorized = True
        
        if authorized:
            target["lock_level"] = LockLevel.NONE
            target["failed_attempts"] = 0
            self._update_identity(target)
            ledger_record("SECURITY_UNLOCK", "SUCCESS", 
                         {"target": target["full_name"], "admin": admin["full_name"]}, "BUNKER_ADMIN")
            print(f"✅ [BUNKER] {target['full_name']} DESBLOQUEADO por {admin['full_name']}")
            return True
        else:
            print(f"⛔ [DENEGADO] {admin['full_name']} sin rango para L{current_lock}")
            ledger_record("UNLOCK_FAIL", "FORBIDDEN", 
                         {"target": target_id, "admin": authorizer_id}, "BUNKER_SECURITY")
            return False