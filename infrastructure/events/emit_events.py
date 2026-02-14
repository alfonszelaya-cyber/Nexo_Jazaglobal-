# ==========================================================
# emit_events.py
# NEXO / ZYRA — CANONICAL EVENT EMITTER
# Núcleo único de eventos
# ==========================================================

import json
import os
import uuid
from datetime import datetime, timezone

# ==========================================================
# CONFIGURACIÓN BASE
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

FILES = {
    "core": "events_core.json",
    "business": "events_business.json",
    "module": "events_modules.json"
}

# ==========================================================
# EMISOR CANÓNICO
# ==========================================================

def emit_events(channel: str, event: dict):
    """
    Emisor único oficial del sistema.
    """

    if channel not in FILES:
        raise ValueError(f"Canal inválido: {channel}")

    if not isinstance(event, dict):
        raise TypeError("El evento debe ser un diccionario")

    path = os.path.join(DATA_DIR, FILES[channel])

    # Carga segura
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []
    else:
        data = []

    if not isinstance(data, list):
        data = []

    record = {
        "id": str(uuid.uuid4()),
        "channel": channel,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event
    }

    data.append(record)

    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        pass
