# ============================================================
# tax_bootstrap.py
# NEXO / ZYRA — FISCAL / IMPUESTOS
# BOOTSTRAP OFICIAL DEL MÓDULO
# NO TOCA CORE | AUTO-REGISTRO PASIVO
# ============================================================

def bootstrap_tax():
    return {
        "module": "TAX",
        "status": "READY",
        "components": [
            "tax_engine",
            "tax_events",
            "tax_validators",
            "tax_rules",
            "tax_health"
        ]
    }


# Auto-registro único
TAX_MODULE = bootstrap_tax()