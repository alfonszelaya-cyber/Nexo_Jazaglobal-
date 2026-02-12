# ============================================================
# ZYRA / NEXO — ENTERPRISE LOGGER
# 10+ AÑOS | CORE SAFE | SIN DEPENDENCIAS CIRCULARES
# Centralizado | Persistente | Escalable
# ============================================================

import os
import json
import threading
from datetime import datetime
from typing import Dict, Any, Optional

# ============================================================
# CONFIGURACIÓN BASE
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

LOG_FILE = os.path.join(DATA_DIR, "zyra_logs.json")

LOG_LEVELS = ("DEBUG", "INFO", "WARN", "ERROR", "CRITICAL")
DEFAULT_LEVEL = "INFO"
MAX_LOG_ENTRIES = 50000

# Lock para evitar corrupción en escritura concurrente
_log_lock = threading.Lock()

# ============================================================
# UTILIDADES INTERNAS
# ============================================================

def _now() -> str:
    return datetime.utcnow().isoformat()

def _load_logs() -> list:
    if not os.path.exists(LOG_FILE):
        return []

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except Exception:
        pass

    return []

def _save_logs(logs: list):
    if len(logs) > MAX_LOG_ENTRIES:
        logs = logs[-MAX_LOG_ENTRIES:]

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

# ============================================================
# LOGGER PRINCIPAL
# ============================================================

def log(
    level: str,
    message: str,
    component: str = "ZYRA_CORE",
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Logger central enterprise.

    - level: DEBUG | INFO | WARN | ERROR | CRITICAL
    - message: Texto principal
    - component: Módulo que genera el log
    - metadata: Datos adicionales opcionales
    """

    if level not in LOG_LEVELS:
        level = DEFAULT_LEVEL

    entry = {
        "timestamp": _now(),
        "level": level,
        "component": component,
        "message": message,
        "metadata": metadata or {}
    }

    # Escritura segura
    with _log_lock:
        logs = _load_logs()
        logs.append(entry)
        _save_logs(logs)

    # Consola estructurada
    print(f"[{level}] [{component}] {message}")

    return entry

# ============================================================
# HELPERS POR NIVEL
# ============================================================

def debug(msg: str, component: str = "ZYRA_CORE", metadata=None):
    return log("DEBUG", msg, component, metadata)

def info(msg: str, component: str = "ZYRA_CORE", metadata=None):
    return log("INFO", msg, component, metadata)

def warn(msg: str, component: str = "ZYRA_CORE", metadata=None):
    return log("WARN", msg, component, metadata)

def error(msg: str, component: str = "ZYRA_CORE", metadata=None):
    return log("ERROR", msg, component, metadata)

def critical(msg: str, component: str = "ZYRA_CORE", metadata=None):
    return log("CRITICAL", msg, component, metadata)

# ============================================================
# CONSULTA (OBSERVABILIDAD)
# ============================================================

def get_logs(limit: int = 100):
    """
    Retorna los últimos N logs.
    """
    logs = _load_logs()
    return logs[-limit:]

# ============================================================
# BOOT LOG
# ============================================================

info("ZYRA Enterprise Logger initialized", component="LOGGER")
