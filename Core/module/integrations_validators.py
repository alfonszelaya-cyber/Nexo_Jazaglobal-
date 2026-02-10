# ============================================================
# integrations_validators.py
# NEXO / ZYRA — INTEGRACIONES EXTERNAS
# VALIDADORES DE INTEGRACIÓN
# ============================================================

def validate_integration(payload: dict) -> bool:
    required = [
        "integration_id",
        "provider",
        "service",
        "endpoint"
    ]

    for key in required:
        if key not in payload:
            return False

    if not payload.get("endpoint").startswith(("http://", "https://")):
        return False

    return True