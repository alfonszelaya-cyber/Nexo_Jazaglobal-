# ============================================================
# shutdown.py
# NEXO / ZYRA — CONTROL DE APAGADO SEGURO (CANÓNICO)
# CORE | AUDITABLE | LONG-TERM
# ============================================================

import os
import json
import sys
from datetime import datetime

# ============================================================
# CONFIGURACIÓN BASE
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
STATE_FILE = os.path.join(DATA_DIR, "shutdown_state.json")

os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(STATE_FILE):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# ============================================================
# UTILIDADES INTERNAS
# ============================================================

def _now():
    return datetime.utcnow().isoformat()

def _load_state():
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def _save_state(data):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# ============================================================
# API CANÓNICA
# ============================================================

def record_shutdown(reason="MANUAL", initiated_by="SYSTEM"):
    """
    Registra un evento de apagado del CORE (inmutable)
    """
    entry = {
        "event": "CORE_SHUTDOWN",
        "reason": reason,
        "initiated_by": initiated_by,
        "timestamp": _now()
    }
    data = _load_state()
    data.append(entry)
    _save_state(data)
    return entry

def safe_exit(code=0, reason="SAFE_EXIT"):
    """
    Apagado seguro del sistema
    """
    record_shutdown(reason=reason)
    sys.exit(code)

# ============================================================
# CONSULTA
# ============================================================

def shutdown_history():
    """
    Devuelve el historial completo de apagados
    """
    return _load_state()