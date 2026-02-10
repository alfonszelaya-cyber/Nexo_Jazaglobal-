# ============================================================
# hygiene_engine.py
# Motor de higiene y control de calidad del CORE ZYRA/NEXO
# ============================================================

import os
import json
from datetime import datetime

# -----------------------------
# Configuración de higiene
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

HYGIENE_FILE = os.path.join(DATA_DIR, "hygiene.json")

# Inicializar archivo si no existe
if not os.path.exists(HYGIENE_FILE):
    with open(HYGIENE_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# -----------------------------
# Funciones de higiene
# -----------------------------
def add_check(location: str, status: str, remarks: str = ""):
    """
    Registra un control de higiene en la ubicación indicada
    """
    data = load_checks()
    entry = {
        "location": location,
        "status": status,
        "remarks": remarks,
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data.append(entry)
    save_checks(data)
    return entry


def load_checks():
    try:
        with open(HYGIENE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []
    return data


def save_checks(data):
    with open(HYGIENE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_all_checks():
    """
    Devuelve todos los controles de higiene registrados
    """
    return load_checks()