# zyra_ledger_hook.py
# NEXO / ZYRA — HOOK CENTRAL DE LEDGER

import os
import json
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

LEDGER_FILE = os.path.join(DATA_DIR, "ledger.json")

def ledger_record(event: str, status: str = "OK", detail=None) -> dict:
    record = {
        "ts": time.time(),
        "event": event,
        "status": status,
        "detail": detail
    }

    data = []
    if os.path.exists(LEDGER_FILE):
        try:
            with open(LEDGER_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = []

    data.append(record)

    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return record


def ledger_read() -> list:
    if os.path.exists(LEDGER_FILE):
        try:
            with open(LEDGER_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []