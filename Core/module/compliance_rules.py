# ============================================================
# compliance_rules.py
# NEXO / ZYRA — COMPLIANCE / REGULACIÓN
# REGLAS DE CUMPLIMIENTO (PLANTILLAS)
# PASIVO | CONFIGURABLE
# ============================================================

# Reglas base de cumplimiento (extensibles)
COMPLIANCE_RULES = {
    "AML": {
        "description": "Anti Money Laundering",
        "required_fields": ["entity", "amount", "country"],
        "threshold": 10000
    },
    "KYC": {
        "description": "Know Your Customer",
        "required_fields": ["entity", "identity_verified"],
        "threshold": None
    }
}

def get_compliance_rule(rule_name: str) -> dict:
    return COMPLIANCE_RULES.get(rule_name.upper(), {})