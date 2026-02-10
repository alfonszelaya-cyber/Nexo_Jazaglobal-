# module_health.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# HEALTH CHECK DEL MÓDULO
# PASIVO | CONSULTADO POR CORE

from datetime import datetime, timezone
from .module_state import MODULE_STATE

def module_health():
    return {
        "module": "LOGISTICA_ASIA",
        "status": MODULE_STATE["status"],
        "active_shipments": MODULE_STATE["active_shipments"],
        "safe_mode": MODULE_STATE["safe_mode"],
        "last_update": MODULE_STATE["last_update"],
        "checked_at": datetime.now(timezone.utc).isoformat()
    }