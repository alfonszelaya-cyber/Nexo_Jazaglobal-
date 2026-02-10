# ============================================================
# system_state.py
# NEXO / ZYRA — ESTADO GLOBAL DEL CORE
# CANÓNICO | ÚNICA FUENTE DE VERDAD
# ============================================================
# Define el estado operativo del CORE
# NO ejecuta lógica
# SOLO expone estado actual
# ============================================================

from datetime import datetime

# ============================================================
# ESTADO SIMPLE (legacy / compatibilidad)
# ============================================================

SYSTEM_STATUS = {
    "core_ready": False,
    "safe_mode": False,
    "last_boot": None,
    "errors": []
}

def set_status(key, value):
    SYSTEM_STATUS[key] = value

def get_status(key):
    return SYSTEM_STATUS.get(key)

def record_error(msg):
    SYSTEM_STATUS["errors"].append(msg)

# ============================================================
# ESTADOS CANÓNICOS DEL CORE
# ============================================================

CORE_STATES = {
    "BOOTING",     # arrancando
    "READY",       # operativo
    "SAFE",        # modo seguro
    "DEGRADED",    # degradado (fallos parciales)
    "SHUTDOWN"     # detenido
}

# ============================================================
# ESTADO GLOBAL CANÓNICO
# ============================================================

_SYSTEM_STATE = {
    "state": "BOOTING",
    "since": datetime.utcnow().isoformat(),
    "reason": None
}

# ============================================================
# API CANÓNICA
# ============================================================

def get_state():
    return _SYSTEM_STATE.copy()

def set_state(state, reason=None):
    if state not in CORE_STATES:
        raise ValueError(f"Estado inválido del CORE: {state}")

    _SYSTEM_STATE["state"] = state
    _SYSTEM_STATE["since"] = datetime.utcnow().isoformat()
    _SYSTEM_STATE["reason"] = reason

    return _SYSTEM_STATE.copy()

def is_ready():
    return _SYSTEM_STATE["state"] == "READY"

def is_safe_mode():
    return _SYSTEM_STATE["state"] in ("SAFE", "DEGRADED")

# ============================================================
# API HUMANA (para MAIN / consola)
# ============================================================

def system_status():
    state = get_state()
    print("\n--- ESTADO DEL SISTEMA ---")
    print(f"Estado : {state['state']}")
    print(f"Desde  : {state['since']}")
    print(f"Razón  : {state['reason']}")

# ============================================================
# NOTAS
# - El CORE decide cuándo cambiar estado
# - Los módulos SOLO consultan
# - No persistente por diseño
# ============================================================