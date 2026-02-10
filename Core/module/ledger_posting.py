# ============================================================
# ledger_posting.py
# NEXO / ZYRA — CONTABILIDAD / LEDGER
# REGISTRO DE ASIENTOS (POSTING)
# PASIVO | SIN AUTOEJECUCIÓN
# ============================================================

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LEDGER_FILE = os.path.join(DATA_DIR, "ledger_entries.json")

def post_ledger_entry(entry: dict):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(entry)

    with open(LEDGER_FILE, "w") as f:
        json.dump(data, f, indent=2)