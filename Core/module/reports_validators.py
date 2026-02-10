# ============================================================
# reports_validators.py
# NEXO / ZYRA — REPORTES & BI
# VALIDADORES DE REPORTES
# ============================================================

def validate_report_payload(payload: dict) -> bool:
    required = [
        "report_id",
        "type",
        "period"
    ]

    for key in required:
        if key not in payload:
            return False

    if not isinstance(payload.get("filters", {}), dict):
        return False

    return True