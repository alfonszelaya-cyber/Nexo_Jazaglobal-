# audit_trail.py
# NEXO / ZYRA — AUDITORÍA & TRAZABILIDAD
# LÍNEA DE TIEMPO DE EVENTOS
# PASIVO

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
TRAIL_FILE = os.path.join(DATA_DIR, "audit_trail.json")

def append_trail(record: dict):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if os.path.exists(TRAIL_FILE):
        with open(TRAIL_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(record)

    with open(TRAIL_FILE, "w") as f:
        json.dump(data, f, indent=2)