# ============================================================
# Core_events.py
# Gestión central de eventos del CORE ZYRA/NEXO
# ============================================================

import os
import json
from datetime import datetime
from zyra_logger import log

# -----------------------------
# Configuración de eventos
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
EVENTS_FILE = os.path.join(DATA_DIR, "events.json")

# -----------------------------
# Funciones de eventos
# -----------------------------
def publish_event(event_type: str, payload: dict):
    """
    Publica un evento en el sistema
    """
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    event_record = {"type": event_type, "payload": payload, "ts": ts}

    try:
        if os.path.exists(EVENTS_FILE):
            with open(EVENTS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        else:
            data = []
    except Exception:
        data = []

    data.append(event_record)

    try:
        with open(EVENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        log("INFO", f"[CORE_EVENTS] Evento publicado: {event_type}")
    except Exception as e:
        log("ERROR", f"[CORE_EVENTS] Error al guardar evento: {e}")

def get_all_events():
    """
    Devuelve todos los eventos registrados
    """
    try:
        with open(EVENTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except Exception as e:
        log("ERROR", f"[CORE_EVENTS] Error al leer eventos: {e}")
        return []

def clear_events():
    """
    Limpia todos los eventos
    """
    try:
        with open(EVENTS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)
        log("INFO", "[CORE_EVENTS] Todos los eventos eliminados")
    except Exception as e:
        log("ERROR", f"[CORE_EVENTS] No se pudo limpiar eventos: {e}")

# -----------------------------
# Función helper para pruebas
# -----------------------------
def test_events():
    publish_event("TEST_EVENT", {"detalle": "Evento de prueba CORE_EVENTS"})
    log("INFO", "[CORE_EVENTS] Test de eventos completado")
