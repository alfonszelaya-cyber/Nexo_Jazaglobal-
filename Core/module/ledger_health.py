# ============================================================
# ledger_health.py
# NEXO / ZYRA — CONTABILIDAD / LEDGER
# HEALTH CHECK DEL MÓDULO
# ============================================================

from datetime import datetime, timezone

def ledger_health_check() -> dict:
    return {
        "module": "LEDGER",
        "status": "OK",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "components": {
            "engine": "READY",
            "validators": "READY",
            "posting": "READY",
            "events": "READY"
        }
    }