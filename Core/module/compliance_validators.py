# ============================================================
# compliance_validators.py
# NEXO / ZYRA — COMPLIANCE / REGULACIÓN
# VALIDADORES DE CUMPLIMIENTO
# ============================================================

def validate_compliance_payload(payload: dict) -> bool:
    required = [
        "entity",
        "ruleset"
    ]

    for key in required:
        if key not in payload:
            return False

    if not isinstance(payload.get("ruleset"), (list, str)):
        return False

    return True