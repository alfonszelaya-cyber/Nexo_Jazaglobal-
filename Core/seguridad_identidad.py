# ============================================================
# NEXO / ZYRA
# SEGURIDAD E IDENTIDAD (CORE CANONICO)
# IDENTIDAD + SEGURIDAD + RIESGO + AUDITORIA
# ============================================================

import os
from datetime import datetime, timedelta
from zyra_bus import emit

# =========================
# CONFIGURACION GLOBAL
# =========================

MAX_FAILED_ATTEMPTS = 3
BLOCK_TIME_MINUTES = 30
RISK_LEVELS = ("LOW", "MEDIUM", "HIGH")

# =========================
# MODELOS BASE
# =========================

class SecurityState:
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    SUSPENDED = "SUSPENDED"


class UserSecurityProfile:
    def __init__(self, user_id, role):
        self.user_id = user_id
        self.role = role
        self.failed_attempts = 0
        self.state = SecurityState.ACTIVE
        self.blocked_until = None
        self.last_event = None
        self.risk_level = "LOW"

    def is_blocked(self):
        if self.state != SecurityState.BLOCKED:
            return False
        if self.blocked_until and datetime.utcnow() > self.blocked_until:
            self.unblock()
            return False
        return True

    def unblock(self):
        self.state = SecurityState.ACTIVE
        self.failed_attempts = 0
        self.blocked_until = None
        self.risk_level = "LOW"

# =========================
# MOTOR DE SEGURIDAD
# =========================

class SecurityEngine:
    def __init__(self):
        self.audit_log = []

    def register_event(self, profile, event_type, metadata=None):
        profile.last_event = event_type
        self._audit(profile, event_type, metadata)
        emit("SECURITY_EVENT", {
            "user": profile.user_id,
            "event": event_type,
            "state": profile.state
        })

    def failed_login(self, profile):
        profile.failed_attempts += 1
        self.register_event(profile, "FAILED_LOGIN")
        if profile.failed_attempts >= MAX_FAILED_ATTEMPTS:
            self.block_user(profile, "MAX_FAILED_ATTEMPTS")

    def unauthorized_action(self, profile, action):
        self.register_event(profile, "UNAUTHORIZED_ACTION", {"action": action})
        self.block_user(profile, "ACTION_OUT_OF_ROLE")

    def risk_detected(self, profile, level):
        if level not in RISK_LEVELS:
            raise ValueError("Invalid risk level")

        profile.risk_level = level
        self.register_event(profile, "RISK_EVENT", {"level": level})

        if level == "HIGH":
            self.block_user(profile, "HIGH_RISK_PREVENTIVE")

    def block_user(self, profile, reason):
        profile.state = SecurityState.BLOCKED
        profile.blocked_until = datetime.utcnow() + timedelta(minutes=BLOCK_TIME_MINUTES)
        self._audit(profile, "USER_BLOCKED", {"reason": reason})
        emit("SECURITY_BLOCK", {
            "user": profile.user_id,
            "reason": reason
        })

    def _audit(self, profile, event, metadata=None):
        self.audit_log.append({
            "ts": datetime.utcnow().isoformat(),
            "user_id": profile.user_id,
            "role": profile.role,
            "state": profile.state,
            "event": event,
            "metadata": metadata or {}
        })

    def get_audit_log(self):
        return self.audit_log

# =========================
# IDENTIDAD (SIMULADA)
# =========================

def get_identidades():
    return [
        {"usuario": "admin", "rol": "SUPER_ADMIN", "estado": "ACTIVO"},
        {"usuario": "operador01", "rol": "OPERADOR", "estado": "ACTIVO"},
        {"usuario": "auditor", "rol": "AUDITOR", "estado": "LIMITADO"},
    ]

def get_roles():
    return [
        {"rol": "SUPER_ADMIN", "nivel": "TOTAL"},
        {"rol": "ADMIN", "nivel": "ALTO"},
        {"rol": "OPERADOR", "nivel": "MEDIO"},
        {"rol": "AUDITOR", "nivel": "LECTURA"},
    ]

def get_logs_acceso():
    return [
        {"usuario": "admin", "evento": "LOGIN", "resultado": "OK"},
        {"usuario": "externo", "evento": "LOGIN", "resultado": "DENEGADO"},
    ]

# =========================
# VISTAS CONSOLA
# =========================

def _header():
    print("=" * 55)
    print("   NEXO / ZYRA — SEGURIDAD E IDENTIDAD (CORE)")
    print("=" * 55)

def _pause():
    input("\nENTER para continuar...")

def vista_identidades():
    _header()
    for i in get_identidades():
        print(f"- {i['usuario']} | {i['rol']} | {i['estado']}")
    emit("SECURITY_VIEW_IDENTITIES")
    _pause()

def vista_roles():
    _header()
    for r in get_roles():
        print(f"- {r['rol']} | {r['nivel']}")
    emit("SECURITY_VIEW_ROLES")
    _pause()

def vista_auditoria():
    _header()
    for l in get_logs_acceso():
        print(f"- {l['usuario']} | {l['evento']} | {l['resultado']}")
    emit("SECURITY_VIEW_AUDIT")
    _pause()

# =========================
# ENTRY UNICO (PARA ROOT)
# =========================

def seguridad_identidad():
    while True:
        _header()
        print("1. Identidades")
        print("2. Roles")
        print("3. Auditoria")
        print("0. Salir")

        op = input("> ").strip()

        if op == "1":
            vista_identidades()
        elif op == "2":
            vista_roles()
        elif op == "3":
            vista_auditoria()
        elif op == "0":
            emit("SECURITY_EXIT")
            break
        else:
            print("Opcion invalida")
            _pause()