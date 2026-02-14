# ============================================================
# ledger_core.py
# Manejo centralizado del ledger del CORE ZYRA
# ============================================================

import os
import json
from domain.system.system_constants import LEDGER_FILE, DATA_DIR
from Core.core_ledger import log

os.makedirs(DATA_DIR, exist_ok=True)

def _load_ledger():
    if not os.path.exists(LEDGER_FILE):
        return []
    try:
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def _save_ledger(entries):
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

def add_entry(entry: dict):
    """
    Agrega una entrada al ledger
    """
    ledger = _load_ledger()
    ledger.append(entry)
    _save_ledger(ledger)
    log("INFO", f"Entrada agregada al ledger: {entry.get('id', 'sin_id')}")

def get_all_entries():
    """
    Devuelve todas las entradas del ledger
    """
    return _load_ledger()
