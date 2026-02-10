# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE REPORTE FINANCIERO
# 10 AÑOS – MULTI PAÍS – MULTI MONEDA
# ============================================================

FINANCIAL_REPORT_TEMPLATE = {
    "report_metadata": {
        "report_id": "auto",
        "version": "1.0",
        "country": "auto",
        "currency": "client_choice",
        "language": "country_default",
        "created_at": "auto",
        "status": "DRAFT"  # DRAFT | FINAL | CANCELLED
    },

    "period": {
        "start_date": "auto",
        "end_date": "auto"
    },

    "financial_summary": {
        "total_income": 0.0,
        "total_expenses": 0.0,
        "net_profit": 0.0,
        "currency_display": "client_choice"
    },

    "financial_items": [
        {
            "category": "",
            "description": "",
            "amount": 0.0,
            "currency": "BASE",
            "tax": 0.0,
            "type": "INCOME"  # INCOME | EXPENSE
        }
    ],

    "zyra_controls": {
        "pre_validate_data": True,
        "audit_ready": True,
        "memory_level": "LONG_TERM",
        "predict_anomalies": True
    },

    "audit_trail": {
        "linked_flows": [],
        "hash": "auto",
        "immutable": True
    }
}

# ============================================================
# FIN DE PLANTILLA DE REPORTE FINANCIERO
# ============================================================