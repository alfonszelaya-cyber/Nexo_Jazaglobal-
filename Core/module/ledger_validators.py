# ============================================================
# ledger_validators.py
# NEXO / ZYRA — CONTABILIDAD / LEDGER
# VALIDADORES CONTABLES
# ============================================================

def validate_ledger_entry(payload: dict) -> bool:
    required = [
        "account_debit",
        "account_credit",
        "amount",
        "currency"
    ]

    for key in required:
        if key not in payload:
            return False

    if payload.get("account_debit") == payload.get("account_credit"):
        return False

    try:
        float(payload.get("amount"))
    except (TypeError, ValueError):
        return False

    return True