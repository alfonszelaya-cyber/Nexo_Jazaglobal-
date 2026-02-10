# ============================================================
# sales_bootstrap.py
# NEXO / ZYRA — VENTAS / POS
# BOOTSTRAP OFICIAL DEL MÓDULO
# NO TOCA MAIN | AUTO-REGISTRO PASIVO
# ============================================================

def bootstrap_sales():
    return {
        "module": "SALES",
        "status": "READY",
        "components": [
            "sales_engine",
            "sales_payments",
            "sales_invoicing",
            "sales_events",
            "sales_validators",
            "sales_alerts",
            "sales_health"
        ]
    }


# Auto-registro único
SALES_MODULE = bootstrap_sales()