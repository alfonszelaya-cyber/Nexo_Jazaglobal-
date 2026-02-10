# ============================================================
# payments_reconciliation.py
# NEXO / ZYRA — PAGOS & BANCOS
# CONCILIACIÓN DE PAGOS
# PASIVO | SIN AUTOEJECUCIÓN
# ============================================================

def reconcile_payment(payment: dict, ledger_entry: dict) -> dict:
    """
    Concilia un pago contra un asiento contable.
    """
    matched = (
        payment.get("amount") == ledger_entry.get("amount")
        and payment.get("currency") == ledger_entry.get("currency")
        and payment.get("reference") == ledger_entry.get("reference")
    )

    return {
        "payment_id": payment.get("payment_id"),
        "ledger_entry_id": ledger_entry.get("entry_id"),
        "status": "MATCHED" if matched else "MISMATCH",
        "details": {
            "payment_amount": payment.get("amount"),
            "ledger_amount": ledger_entry.get("amount")
        }
    }