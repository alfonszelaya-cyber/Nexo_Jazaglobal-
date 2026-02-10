# module_safe_mode.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# MODO SAFE / DEGRADED DEL MÓDULO
# PASIVO | CONTROLADO POR CORE

from .module_state import MODULE_STATE

def enter_safe_mode(reason: str = None):
    MODULE_STATE["status"] = "SAFE_MODE"
    MODULE_STATE["safe_mode"] = True
    if reason:
        MODULE_STATE["errors"].append({"safe_mode_reason": reason})

def exit_safe_mode():
    MODULE_STATE["status"] = "INIT"
    MODULE_STATE["safe_mode"] = False