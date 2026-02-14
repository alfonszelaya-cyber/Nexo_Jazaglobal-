import json
import os
import uuid
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

FILES = {
    "core": "events_core.json",
    "business": "events_business.json",
    "module": "events_modules.json"
}

# ============================
# EMISOR CANÓNICO DE EVENTOS
# ============================
def emit_event(channel: str, event: dict):
    """
    Registra un evento por canal (core | business | module)
    Diseño:
    - No ejecuta lógica
    - No imprime
    - No depende de otros módulos
    - Escalable a auditoría y análisis futuro
    """

    if channel not in FILES:
        raise ValueError(f"Canal inválido: {channel}")

    path = os.path.join(DATA_DIR, FILES[channel])

    # ----------------------------
    # Carga segura
    # ----------------------------
    if not os.path.exists(path):
        data = []
    else:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []

    if not isinstance(data, list):
        data = []

    # ----------------------------
    # Normalización del evento
    # ----------------------------
    record = {
        "id": str(uuid.uuid4()),
        "channel": channel,
        "ts": datetime.now(timezone.utc).isoformat(),
        "event": event
    }

    data.append(record)

    # ----------------------------
    # Persistencia segura
    # ----------------------------
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        # Failsafe silencioso (no tumba el CORE)
        pass