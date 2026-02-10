# ============================================================
# ledger_read.py
# Lectura de entradas del ledger del CORE ZYRA/NEXO
# ============================================================

import os
import json
import datetime

# -----------------------------
# Configuración del ledger
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LEDGER_FILE = os.path.join(DATA_DIR, "ledger.json")
os.makedirs(DATA_DIR, exist_ok=True)

# -----------------------------
# Funciones de lectura
# -----------------------------
def get_all_entries():
    """
    Devuelve todas las entradas del ledger
    """
    try:
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except Exception:
        return []

def get_entries_by_type(tipo: str):
    """
    Devuelve todas las entradas filtradas por tipo
    """
    all_entries = get_all_entries()
    return [e for e in all_entries if e.get("entry", {}).get("tipo") == tipo]

def get_entries_by_date_range(start_date: str, end_date: str):
    """
    Devuelve todas las entradas entre fechas dadas (YYYY-MM-DD)
    """
    all_entries = get_all_entries()
    filtered = []
    for e in all_entries:
        ts = e.get("ts")
        if not ts:
            continue
        entry_date = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
        if start_date:
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            if entry_date < start:
                continue
        if end_date:
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            if entry_date > end:
                continue
        filtered.append(e)
    return filtered