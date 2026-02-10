# ============================================================
# zyra_logger.py
# Registro central de logs del CORE ZYRA/NEXO
# ============================================================

import os
import json
from datetime import datetime
from core.system_constants import LOGS_FILE, LOG_LEVELS, DATA_DIR, DEFAULT_LOG_LEVEL

# Asegura que el directorio DATA exista
os.makedirs(DATA_DIR, exist_ok=True)

def log(level: str, message: str, component: str = "ZYRA_CORE"):
    """
    Logger central del CORE.
    - level: Nivel de log (DEBUG, INFO, WARN, ERROR, CRITICAL)
    - message: Mensaje de log
    - component: Componente que genera el log
    """
    if level not in LOG_LEVELS:
        level = DEFAULT_LOG_LEVEL

    ts = datetime.now().isoformat()
    entry = {
        "timestamp": ts,
        "level": level,
        "component": component,
        "message": message
    }

    # Escribir en consola
    print(f"[{level}] [{component}] {message} @ {ts}")

    # Escribir en archivo JSON
    logs = []
    try:
        if os.path.exists(LOGS_FILE):
            with open(LOGS_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
    except Exception:
        logs = []

    logs.append(entry)

    # Limitar tamaño máximo de archivo
    MAX_LOG_ENTRIES = 20000
    if len(logs) > MAX_LOG_ENTRIES:
        logs = logs[-MAX_LOG_ENTRIES:]

    with open(LOGS_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

    return entry

# Función de prueba rápida para el CORE
def boot():
    log("INFO", "Logger ZYRA cargado y listo", "ZYRA_CORE")