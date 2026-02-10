# core/system_constants.py
# ============================================================
# Constantes globales del CORE ZYRA/NEXO
# ============================================================

import os

# -----------------------------
# Identidad del CORE
# -----------------------------
CORE_NAME = "ZYRA"
CORE_VERSION = "1.0.0"

# -----------------------------
# Directorios y archivos
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
EVENTS_FILE = os.path.join(DATA_DIR, "events.json")
LEDGER_FILE = os.path.join(DATA_DIR, "ledger.json")
LOGS_FILE = os.path.join(DATA_DIR, "logs.json")

# Crear carpeta data si no existe
os.makedirs(DATA_DIR, exist_ok=True)

# -----------------------------
# Estados del sistema
# -----------------------------
STATES = ("INIT", "READY", "DEGRADED", "SHUTDOWN")
VALID_STATES_DOC = ("BORRADOR", "EMITIDO", "CONFIRMADO", "CANCELADO")

# -----------------------------
# Monedas permitidas
# -----------------------------
VALID_CURRENCIES = ("USD", "BTC")

# -----------------------------
# Configuración de logs y eventos
# -----------------------------
LOG_LEVELS = ("DEBUG", "INFO", "WARN", "ERROR", "CRITICAL")