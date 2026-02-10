# ============================================================
# event_dispatcher.py
# Despachador de eventos para CORE ZYRA/NEXO
# ============================================================

import os
import json
import datetime

# -----------------------------
# Configuración del archivo de eventos
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
EVENTS_FILE = os.path.join(DATA_DIR, "events.json")
os.makedirs(DATA_DIR, exist_ok=True)

_event_hooks = []

# -----------------------------
# Registro y gestión de hooks de eventos
# -----------------------------
def register_event_hook(hook_callable):
    """
    Registra un hook que se ejecuta cuando se publica un evento
    """
    if callable(hook_callable):
        _event_hooks.append(hook_callable)

def remove_event_hook(hook_callable):
    """
    Remueve un hook registrado
    """
    if hook_callable in _event_hooks:
        _event_hooks.remove(hook_callable)

def clear_event_hooks():
    """
    Limpia todos los hooks registrados
    """
    _event_hooks.clear()

# -----------------------------
# Funciones de eventos
# -----------------------------
def dispatch_event(event: dict):
    """
    Despacha un evento: guarda en archivo y dispara hooks
    """
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    event_record = {"event": event, "ts": ts}

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
    except Exception as e:
        print(f"[EVENT_DISPATCHER] Error guardando evento: {e}")

    # Disparar hooks registrados
    trigger_event_hooks(event_record)

def trigger_event_hooks(event_record: dict):
    """
    Ejecuta todos los hooks registrados para un evento
    """
    for hook in _event_hooks:
        try:
            hook(event_record)
        except Exception as e:
            print(f"[EVENT_DISPATCHER] Error en hook: {e}")

# -----------------------------
# Función de prueba rápida
# -----------------------------
def test_event_dispatcher():
    def sample_hook(event_record):
        print(f"[HOOK] Evento recibido: {event_record}")

    register_event_hook(sample_hook)
    dispatch_event({"tipo": "TEST_EVENT", "detalle": "Prueba de dispatcher"})
    clear_event_hooks()