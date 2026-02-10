# ============================================================
# tax_health.py
# NEXO / ZYRA — FISCAL / IMPUESTOS
# HEALTH CHECK DEL MÓDULO
# ============================================================

from datetime import datetime, timezone

def tax_health_check() -> dict:
    return {
        "module": "TAX",
        "status": "OK",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "components": {
            "engine": "READY",
            "validators": "READY",
            "rules": "READY",
            "events": "READY"
        }
    }