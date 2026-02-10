# ============================================================
# event_registry.py
# NEXO / ZYRA — EVENT REGISTRY CANÓNICO
# MAPEO ÚNICO DE EVENTOS → HANDLERS
# SIN LÓGICA | SIN EJECUCIÓN | DEFINITIVO
# ============================================================

EVENT_REGISTRY = {

    # ================= CORE =================
    "CORE_INIT": [],
    "CORE_SHUTDOWN": [],
    "CORE_ERROR": [],

    # ================= SEGURIDAD =================
    "AUTH_LOGIN": [],
    "AUTH_LOGOUT": [],
    "AUTH_FAILED": [],

    # ================= FINANZAS =================
    "FIN_TX_CREATED": [],
    "FIN_TX_APPROVED": [],
    "FIN_TX_REJECTED": [],

    # ================= OPERACIONES =================
    "OPS_ORDER_CREATED": [],
    "OPS_ORDER_DISPATCHED": [],
    "OPS_ORDER_DELIVERED": [],

    # ================= RADAR / ZYRA =================
    "RADAR_ANALYSIS_CREATED": [],
    "RADAR_RECOMMENDATION_READY": [],
    "RADAR_DECISION_TAKEN": []
}

# ============================================================
# REGLAS
# - Las claves son TIPOS CANÓNICOS de evento
# - Los valores son listas de handlers (inyectados en runtime)
# - Este archivo NO ejecuta nada
# - main solo lo importa
# - No debe modificarse sin orden explícita
# ============================================================