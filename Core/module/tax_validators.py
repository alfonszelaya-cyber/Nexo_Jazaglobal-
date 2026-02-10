# ============================================================
# tax_validators.py
# NEXO / ZYRA — FISCAL / IMPUESTOS
# VALIDADORES FISCALES
# ============================================================

def validate_tax_payload(payload: dict) -> bool:
    required = [
        "base_amount",
        "tax_rate",
        "country",
        "currency"
    ]

    for key in required:
        if key not in payload:
            return False

    try:
        float(payload.get("base_amount"))
        float(payload.get("tax_rate"))
    except (TypeError, ValueError):
        return False

    if payload.get("tax_rate") < 0:
        return False

    return True