# module_shutdown.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# CIERRE LIMPIO DEL MÓDULO
# PASIVO | LLAMADO POR CORE

from datetime import datetime, timezone
from .module_state import MODULE_STATE

def shutdown_module():
    MODULE_STATE["status"] = "SHUTDOWN"
    MODULE_STATE["last_update"] = datetime.now(timezone.utc).isoformat()
    return {
        "module": "LOGISTICA_ASIA",
        "status": "SHUTDOWN",
        "ts": MODULE_STATE["last_update"]
    }