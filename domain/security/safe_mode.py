# ============================================================
# safe_mode.py
# NEXO / ZYRA — SAFE MODE CONTROLLER CANÓNICO
# CORE | ESTABLE | +10 AÑOS
# ============================================================

import os
import json
from datetime import datetime

# ============================================================
# MODOS SOPORTADOS
# ============================================================
MODE_NORMAL = "NORMAL"
MODE_SAFE = "SAFE"
MODE_DEGRADED = "DEGRADED"

# ============================================================
# CONFIGURACIÓN DE PERSISTENCIA
# ============================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
STATE_FILE = os.path.join(DATA_DIR, "safe_mode.json")
os.makedirs(DATA_DIR, exist_ok=True)

# ============================================================
# ESTADO POR DEFECTO
# ============================================================
_DEFAULT_STATE = {
    "mode": MODE_NORMAL,
    "reason": None,
    "timestamp": None,
    "activated_by": None
}

# ============================================================
# ESTADO EN MEMORIA (FUENTE RÁPIDA)
# ============================================================
_CURRENT_STATE = _DEFAULT_STATE.copy()

# ============================================================
# HELPERS INTERNOS
# ============================================================
def _load_state():
    try:
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
    except Exception:
        pass
    return _DEFAULT_STATE.copy()


def _save_state(state: dict):
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except Exception:
        pass


def _set_state(mode: str, reason: str | None, activated_by: str):
    global _CURRENT_STATE
    state = {
        "mode": mode,
        "reason": reason,
        "timestamp": datetime.utcnow().isoformat(),
        "activated_by": activated_by
    }
    _CURRENT_STATE = state
    _save_state(state)

# ============================================================
# API PÚBLICA — SETTERS
# ============================================================
def activate_safe_mode(reason: str, activated_by: str = "SYSTEM"):
    _set_state(MODE_SAFE, reason, activated_by)


def activate_degraded_mode(reason: str, activated_by: str = "SYSTEM"):
    _set_state(MODE_DEGRADED, reason, activated_by)


def restore_normal_mode(activated_by: str = "SYSTEM"):
    _set_state(MODE_NORMAL, None, activated_by)

# ============================================================
# API PÚBLICA — GETTERS
# ============================================================
def get_mode() -> str:
    return _CURRENT_STATE.get("mode", MODE_NORMAL)


def is_safe_mode() -> bool:
    return get_mode() == MODE_SAFE


def is_degraded_mode() -> bool:
    return get_mode() == MODE_DEGRADED


def get_mode_snapshot() -> dict:
    """
    Snapshot completo del estado del CORE
    """
    disk_state = _load_state()
    return {
        "memory": _CURRENT_STATE,
        "disk": disk_state
    }

# ============================================================
# INICIALIZACIÓN AUTOMÁTICA
# ============================================================
_CURRENT_STATE = _load_state()

# ============================================================
# GARANTÍAS DE DISEÑO
# ============================================================
# - Sin prints
# - Sin tests
# - Sin dependencias circulares
# - Persistente para auditoría
# - Seguro ante fallos
# - Compatible con error_handler
# - Diseñado para operación continua (+10 años)
# ============================================================