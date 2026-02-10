# ============================================================
# tax_engine.py
# NEXO / ZYRA — FISCAL / IMPUESTOS
# MOTOR FISCAL CENTRAL
# PASIVO | EVENT-DRIVEN | SIN AUTOEJECUCIÓN
# ============================================================

from datetime import datetime, timezone

def calculate_taxes(payload: dict) -> dict:
    """
    Calcula impuestos base (sin persistir).
    """
    return {
        "tax_id": payload.get("tax_id"),
        "base_amount": payload.get("base_amount", 0),
        "tax_rate": payload.get("tax_rate", 0),
        "tax_amount": payload.get("base_amount", 0) * payload.get("tax_rate", 0),
        "country": payload.get("country"),
        "currency": payload.get("currency", "USD"),
        "module": payload.get("module"),
        "status": "CALCULATED",
        "ts": datetime.now(timezone.utc).isoformat()
    }