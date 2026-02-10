# module_state.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# ESTADO GLOBAL DEL MÓDULO
# INMUTABLE | CONTROLADO POR CORE

MODULE_STATE = {
    "status": "INIT",          # INIT | IN_TRANSIT | CUSTOMS | DELIVERED | ERROR | SAFE_MODE
    "last_event": None,        # Último evento procesado
    "last_update": None,       # Timestamp UTC
    "active_shipments": 0,     # Conteo rápido
    "errors": [],              # Errores recientes
    "safe_mode": False         # Flag SAFE
}