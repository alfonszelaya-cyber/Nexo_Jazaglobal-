import json, os
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

FILES = {
    "core": "events_core.json",
    "business": "events_business.json",
    "module": "events_modules.json"
}

def emit_event(channel: str, event: dict):
    path = os.path.join(DATA_DIR, FILES[channel])

    # Si no existe → crear lista vacía
    if not os.path.exists(path):
        data = []
    else:
        with open(path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    # Blindaje: si alguien dejó un dict, lo reseteamos
    if not isinstance(data, list):
        data = []

    event["ts"] = datetime.now(timezone.utc).isoformat()
    data.append(event)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)