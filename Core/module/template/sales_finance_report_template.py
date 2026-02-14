# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE REPORTE FINANCIERO / VENTAS
# 10 AÑOS – MULTI PAÍS – MULTI MONEDA
# ============================================================

SALES_FINANCE_REPORT_TEMPLATE = {

    "report_metadata": {
        "report_id": "auto",
        "report_type": "SALES_FINANCE",   # SALES_FINANCE | TAX | CUSTOM
        "version": "1.0",
        "country": "auto",
        "created_by": "ZYRA",
        "created_at": "auto",
        "period": {
            "start_date": "auto",
            "end_date": "auto"
        },
        "status": "DRAFT"                # DRAFT | FINAL | ARCHIVED
    },

    "company_info": {
        "name": "",
        "tax_id": "",
        "address": "",
        "currency": "USD"
    },

    "sales_summary": [
        {
            "product_id": "",
            "description": "",
            "units_sold": 0,
            "unit_price": 0.0,
            "total_sales": 0.0,
            "currency": "USD"
        }
    ],

    "financial_summary": {
        "revenue_total": 0.0,
        "tax_total": 0.0,
        "discounts_total": 0.0,
        "net_total": 0.0,
        "currency": "USD"
    },

    "zyra_supervision": {
        "check_compliance": True,
        "auto_flag_errors": True,
        "memory_level": "LONG_TERM",
        "audit_trail_enabled": True
    },

    "audit_trail": {
        "linked_documents": [],
        "hash": "auto",
        "immutable": True
    }
}

# ============================================================
# FIN DE PLANTILLA
# ============================================================