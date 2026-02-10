# =========================================
# zyra_bus.py
# BUS DE EVENTOS CANÓNICO ZYRA
# Persistente + Suscriptores (NO rompe lo existente)
# =========================================

import json
import os
from datetime import datetime

# Rutas base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

EVENTS_FILE = os.path.join(DATA_DIR, "events.json")

# ============================
# SUBSCRIPTORES EN MEMORIA
# ============================
_subscribers = {}

def subscribe(event_name, handler):
    """
    Permite que otros módulos se suscriban a eventos específicos
    """
    if event_name not in _subscribers:
        _subscribers[event_name] = []
    _subscribers[event_name].append(handler)

# ============================
# EMITIR EVENTO (CANÓNICO)
# ============================
def emit(event, source="SYSTEM", payload=None):
    """
    Compatible con:
    - emit("EVENTO", source="X", payload={})
    - emit({ "event": "...", "source": "...", "payload": {...} })
    """

    if isinstance(event, dict):
        registro = {
            "event": event.get("event"),
            "source": event.get("source", source),
            "payload": event.get("payload"),
            "ts": datetime.now().isoformat()
        }
    else:
        registro = {
            "event": event,
            "source": source,
            "payload": payload,
            "ts": datetime.now().isoformat()
        }

    # -------------------------
    # PERSISTENCIA
    # -------------------------
    data = []
    if os.path.exists(EVENTS_FILE):
        try:
            with open(EVENTS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        except Exception:
            data = []

    data.append(registro)

    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # -------------------------
    # DISPATCH A SUBSCRIPTORES
    # -------------------------
    event_name = registro.get("event")
    if event_name in _subscribers:
        for handler in _subscribers[event_name]:
            try:
                handler(registro)
            except Exception as e:
                print(f"[ZYRA BUS ERROR] {e}")

    return registro