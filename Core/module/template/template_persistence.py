# ============================================================
# ZYRA / NEXO
# TEMPLATE PERSISTENCE CANÓNICO
# Guarda instancias activadas de plantillas
# 10+ AÑOS – LONG TERM MEMORY
# ============================================================

import os
import json
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

TEMPLATE_LEDGER = os.path.join(DATA_DIR, "template_ledger.json")

def _now():
    return datetime.now(timezone.utc).isoformat()

def _load():
    if not os.path.exists(TEMPLATE_LEDGER):
        return []
    try:
        with open(TEMPLATE_LEDGER, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def _save(data):
    with open(TEMPLATE_LEDGER, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def persist_template_instance(template_name: str, instance: dict, core_result: dict):
    """
    Guarda una instancia ejecutada de plantilla
    """

    ledger = _load()

    record = {
        "template": template_name,
        "timestamp": _now(),
        "instance": instance,
        "core_result": core_result
    }

    ledger.append(record)
    _save(ledger)

    return {
        "status": "SAVED",
        "template": template_name,
        "timestamp": record["timestamp"]
    }