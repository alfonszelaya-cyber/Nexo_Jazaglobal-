# ============================================================
# ZYRA / NEXO
# TEMPLATE VALIDATOR CANÓNICO
# Valida estructura mínima de plantillas activadas
# 10+ AÑOS – CORE SAFE
# ============================================================

REQUIRED_KEYS = {
    "flow_metadata": ["flow_id", "status"],
    "report_metadata": ["report_id", "status"]
}

def validate_template_instance(instance: dict) -> dict:
    """
    Valida estructura base de una instancia de plantilla.
    No valida negocio, solo forma.
    """

    errors = []

    if not isinstance(instance, dict):
        return {"valid": False, "errors": ["instance_not_dict"]}

    # Validar metadatos
    if "flow_metadata" in instance:
        for k in REQUIRED_KEYS["flow_metadata"]:
            if k not in instance["flow_metadata"]:
                errors.append(f"missing_flow_metadata:{k}")

    if "report_metadata" in instance:
        for k in REQUIRED_KEYS["report_metadata"]:
            if k not in instance["report_metadata"]:
                errors.append(f"missing_report_metadata:{k}")

    # Validar audit trail si existe
    if "audit_trail" in instance:
        if not isinstance(instance["audit_trail"], dict):
            errors.append("audit_trail_invalid")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }