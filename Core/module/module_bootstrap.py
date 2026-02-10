# module_bootstrap.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# BOOTSTRAP DEL MÓDULO
# ÚNICO PUNTO DE ENTRADA DEL MÓDULO

from .module_contracts import MODULE_CONTRACT
from .module_registry import MODULE_REGISTRY
from .module_version import MODULE_VERSION
from .module_integrity import check_module_integrity
from .module_state import MODULE_STATE

def bootstrap():
    if not check_module_integrity():
        MODULE_STATE["status"] = "ERROR"
        return False

    MODULE_STATE["status"] = "INIT"
    return {
        "contract": MODULE_CONTRACT,
        "registry": MODULE_REGISTRY,
        "version": MODULE_VERSION,
        "state": MODULE_STATE
    }