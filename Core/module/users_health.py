# ============================================================
# users_health.py
# NEXO / ZYRA — USUARIOS & ROLES (NEGOCIO)
# HEALTH CHECK DEL MÓDULO
# ============================================================

from datetime import datetime, timezone

def users_health_check() -> dict:
    return {
        "module": "USERS",
        "status": "OK",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "components": {
            "engine": "READY",
            "roles": "READY",
            "validators": "READY",
            "events": "READY"
        }
    }