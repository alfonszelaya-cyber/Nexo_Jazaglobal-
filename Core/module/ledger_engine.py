# ============================================================
# ledger_engine.py
# NEXO / ZYRA — CONTABILIDAD / LEDGER
# MOTOR CONTABLE CENTRAL
# PASIVO | EVENT-DRIVEN | SIN AUTOEJECUCIÓN
# ============================================================

from datetime import datetime, timezone
from decimal import Decimal

def create_ledger_entry(payload: dict) -> dict:
    """
    Crea un asiento contable base (sin persistir).
    """
    return {
        "entry_id": payload.get("entry_id"),
        "date": payload.get("date") or datetime.now(timezone.utc).date().isoformat(),
        "account_debit": payload.get("account_debit"),
        "account_credit": payload.get("account_credit"),
        "amount": str(Decimal(payload.get("amount", "0"))),
        "currency": payload.get("currency", "USD"),
        "reference": payload.get("reference"),
        "module": payload.get("module"),
        "status": "POSTED",
        "ts": datetime.now(timezone.utc).isoformat()
    }