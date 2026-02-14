# ==========================================================
# event_bus.py
# NEXO / ZYRA — CANONICAL EVENT BUS
# Arquitectura Enterprise | Escalable 10+ años | Inmutable
# ==========================================================

import json
import os
import uuid
from datetime import datetime, timezone
from typing import Dict, Any

# ==========================================================
# CONFIGURACIÓN BASE
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

CHANNEL_FILES = {
    "core": "events_core.json",
    "business": "events_business.json",
    "module": "events_modules.json"
}

# ==========================================================
# UTILIDADES INTERNAS
# ==========================================================

def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()

def _safe_load(path: str):
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def _safe_save(path: str, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        # Failsafe: nunca tumbar el sistema por error de disco
        pass

# ==========================================================
# EMISOR CANÓNICO
# ==========================================================

def emit_event(channel: str, event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Emite un evento estructurado y lo persiste por canal.

    Reglas:
    - No ejecuta lógica de negocio
    - No imprime logs
    - No depende de otros módulos
    - No rompe el sistema si falla persistencia
    - Preparado para migración futura a broker real (Redis, Kafka, etc.)
    """

    if not isinstance(channel, str) or channel not in CHANNEL_FILES:
        raise ValueError(f"Canal inválido: {channel}")

    if not isinstance(event, dict):
        raise TypeError("El evento debe ser un diccionario")

    path = os.path.join(DATA_DIR, CHANNEL_FILES[channel])
    data = _safe_load(path)

    record = {
        "id": str(uuid.uuid4()),
        "channel": channel,
        "timestamp": _now_utc(),
        "event": event
    }

    data.append(record)
    _safe_save(path, data)

    return record
