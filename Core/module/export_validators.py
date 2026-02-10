# ============================================================
# export_validators.py
# NEXO / ZYRA — EXPORT VALIDATORS
# ============================================================

def validate_export(data: dict) -> bool:
    required = ["origin", "destination", "product", "quantity"]

    for key in required:
        if key not in data:
            return False

    return True