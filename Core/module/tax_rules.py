# ============================================================
# tax_rules.py
# NEXO / ZYRA — FISCAL / IMPUESTOS
# REGLAS FISCALES POR PAÍS
# PASIVO | CONFIGURABLE
# ============================================================

# Reglas base (plantillas). Se pueden extender por país.
TAX_RULES = {
    "NI": {  # Nicaragua
        "VAT": 0.15,
        "INCOME": 0.30
    },
    "US": {  # Estados Unidos (genérico)
        "VAT": 0.00,
        "INCOME": 0.21
    }
}

def get_tax_rate(country: str, tax_type: str) -> float:
    country = country.upper()
    tax_type = tax_type.upper()

    if country not in TAX_RULES:
        return 0.0

    return TAX_RULES[country].get(tax_type, 0.0)