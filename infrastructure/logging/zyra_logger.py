# ==============================================
# zyra_logger.py
# Módulo de logging central del CORE ZYRA/NEXO
# ==============================================

import os
import datetime
import json

# -----------------------------
# Configuración de logging
# -----------------------------
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "logs_hook.json")

LOG_LEVELS = ("DEBUG", "INFO", "WARN", "ERROR", "CRITICAL")

# -----------------------------
# Función para loguear eventos
# -----------------------------
def log(level: str, message: str):
    """
    Registra un evento en el log central.
    """
    if level not in LOG_LEVELS:
        level = "INFO"

    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"ts": ts, "level": level, "message": message}

    # Guardar en archivo JSON
    try:
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2)
        
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []

        data.append(entry)

        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[ZYRA_LOGGER ERROR] No se pudo registrar log: {e}")

    # También imprimir en consola
    print(f"[{level}] {ts} | {message}")

# -----------------------------
# Funciones helper por nivel
# -----------------------------
def debug(msg): log("DEBUG", msg)
def info(msg): log("INFO", msg)
def warn(msg): log("WARN", msg)
def error(msg): log("ERROR", msg)
def critical(msg): log("CRITICAL", msg)

# -----------------------------
# Inicialización automática
# -----------------------------
info("ZYRA Logger inicializado correctamente")