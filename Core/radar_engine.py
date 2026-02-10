# ============================================================
# radar_engine.py
# Motor de radar VIP y seguimiento del CORE ZYRA/NEXO
# ============================================================

import os
import json
import datetime

# -----------------------------
# Configuración del radar
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RADAR_FILE = os.path.join(DATA_DIR, "radar_vip.json")
os.makedirs(DATA_DIR, exist_ok=True)

# Inicializar archivo de radar si no existe
if not os.path.exists(RADAR_FILE):
    with open(RADAR_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# -----------------------------
# Funciones de radar VIP
# -----------------------------
def add_radar_entry(entry: dict):
    """
    Agrega una entrada al radar VIP
    """
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry_record = {"entry": entry, "ts": ts}

    try:
        with open(RADAR_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []

    data.append(entry_record)

    try:
        with open(RADAR_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

def get_all_radar_entries():
    """
    Retorna todas las entradas del radar VIP
    """
    try:
        with open(RADAR_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except Exception:
        return []

def clear_radar_entries():
    """
    Limpia todas las entradas del radar VIP
    """
    try:
        with open(RADAR_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)
    except Exception:
        pass

# ------------------------------------------------------------
# Alias estándar esperado por NEXO/ZYRA
# ------------------------------------------------------------
def registrar_evento(
    tipo: str,
    origen: str,
    descripcion: str,
    nivel: int = 1,
    referencia: str | None = None
):
    """
    Función genérica de registro de eventos para Radar VIP.
    Internamente usa add_radar_entry.
    """
    evento = {
        "tipo": tipo,
        "origen": origen,
        "descripcion": descripcion,
        "nivel": nivel,
        "referencia": referencia
    }
    add_radar_entry(evento)
    return evento