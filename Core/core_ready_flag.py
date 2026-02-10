# ============================================================
# core_ready_flag.py
# Manejo del indicador de readiness del CORE ZYRA
# ============================================================

_ready_flag = False

def set_ready(value: bool):
    """
    Establece el indicador de CORE listo (True/False)
    """
    global _ready_flag
    _ready_flag = bool(value)

def is_ready() -> bool:
    """
    Devuelve True si el CORE está listo
    """
    return _ready_flag