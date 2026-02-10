# ============================================================
# zyra_logs_hook.py
# Hook avanzado de logs para CORE ZYRA/NEXO
# ============================================================

import os
import json
import datetime

# -----------------------------
# Configuración del archivo de logs
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_FILE = os.path.join(DATA_DIR, "zyra_logs.json")
os.makedirs(DATA_DIR, exist_ok=True)

_hooks = []

# -----------------------------
# Registro y gestión de hooks
# -----------------------------
def register_log_hook(hook_callable):
    if callable(hook_callable):
        _hooks.append(hook_callable)

def remove_log_hook(hook_callable):
    if hook_callable in _hooks:
        _hooks.remove(hook_callable)

def clear_log_hooks():
    _hooks.clear()

# -----------------------------
# Función principal de log
# -----------------------------
def log(event: str, level: str = "INFO", source: str = "SYSTEM", extra: dict | None = None):
    ts = datetime.datetime.utcnow().isoformat()
    entry = {
        "event": event,
        "level": level,
        "source": source,
        "extra": extra or {},
        "ts": ts
    }
    add_log(entry)
    return entry

# -----------------------------
# Función interna de almacenamiento
# -----------------------------
def add_log(entry: dict):
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        else:
            data = []
    except:
        data = []

    data.append(entry)

    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[ZYRA_LOGS_HOOK] Error guardando logs: {e}")

    trigger_hooks(entry)

def trigger_hooks(log_record: dict):
    for hook in _hooks:
        try:
            hook(log_record)
        except Exception as e:
            print(f"[ZYRA_LOGS_HOOK] Error en hook: {e}")

# -----------------------------
# Auto-test
# -----------------------------
if __name__ == "__main__":
    def sample_hook(log_entry):
        print(f"[HOOK] Entrada de log: {log_entry}")

    register_log_hook(sample_hook)
    log("PRUEBA_EVENTO", level="INFO", source="TEST_CORE", extra={"detalle": "Prueba completa"})
    clear_log_hooks()