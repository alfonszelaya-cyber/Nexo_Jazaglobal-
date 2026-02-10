# ============================================================
# payments_validators.py
# NEXO / ZYRA — PAGOS & BANCOS
# VALIDADORES DE PAGOS
# ============================================================

def validate_payment(payload: dict) -> bool:
    required = [
        "payment_id",
        "amount",
        "currency",
        "method"
    ]

    for key in required:
        if key not in payload:
            return False

    try:
        float(payload.get("amount"))
    except (TypeError, ValueError):
        return False

    if payload.get("amount", 0) <= 0:
        return False

    return True