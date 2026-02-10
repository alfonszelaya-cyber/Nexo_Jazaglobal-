# import_history_engine.py
# NEXO / ZYRA — IMPORTACIONES
# HISTORIAL DE DECISIONES
# PASIVO | EVENT-DRIVEN

import json
import os
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
HISTORY_FILE = os.path.join(DATA_DIR, "import_history.json")


def register_import_decision(record: dict):
    """
    Guarda el historial de decisiones de importación.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    record["ts"] = datetime.now(timezone.utc).isoformat()
    data.append(record)

    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)