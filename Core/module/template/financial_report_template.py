# ============================================================
# ZYRA / NEXO
# FINANCIAL REPORT TEMPLATE — ENTERPRISE 3.0
# Multi-Country | Multi-Currency | Audit-Grade | BI Ready
# ============================================================

FINANCIAL_REPORT_TEMPLATE_V3 = {

    "report_metadata": {
        "report_id": "auto_uuid",
        "report_type": "GENERAL_FINANCIAL",   # GENERAL | TAX | AUDIT | CUSTOM
        "schema_version": "3.0",
        "core_version": "auto",
        "country": "auto_detected",
        "base_currency": "USD",
        "presentation_currency": "client_choice",
        "language": "auto",
        "generated_by": "ZYRA_ENGINE",
        "generated_at": "auto_utc",
        "status": "DRAFT",  # DRAFT | FINAL | ARCHIVED | LOCKED
        "data_integrity_hash": "auto_hash"
    },

    "entity_info": {
        "entity_id": "auto",
        "entity_type": "CORPORATION",  # NATURAL | CORPORATION | GOVERNMENT
        "legal_name": "",
        "tax_id": "",
        "registered_address": "",
        "compliance_profile": "STANDARD"
    },

    "reporting_period": {
        "fiscal_year": "auto",
        "start_date": "auto",
        "end_date": "auto",
        "timezone": "UTC"
    },

    "financial_summary": {
        "total_income": 0.0,
        "total_expenses": 0.0,
        "gross_profit": 0.0,
        "operational_costs": 0.0,
        "net_profit": 0.0,
        "tax_estimation": 0.0,
        "currency": "base_currency"
    },

    "financial_breakdown": [
        {
            "category_code": "",
            "category_name": "",
            "type": "INCOME",  # INCOME | EXPENSE | TAX | ADJUSTMENT
            "amount": 0.0,
            "currency": "BASE",
            "tax_applicable": True,
            "linked_flow_ids": [],
            "risk_flag": False
        }
    ],

    "controls": {
        "zyra_pre_validation": True,
        "anomaly_detection": True,
        "auto_reconciliation": True,
        "cross_module_consistency_check": True,
        "compliance_level": "STRICT"
    },

    "analytics_layer": {
        "trend_analysis_enabled": True,
        "variance_analysis_enabled": True,
        "forecast_projection_enabled": True,
        "risk_score": 0.0
    },

    "audit_trail": {
        "immutable": True,
        "linked_documents": [],
        "event_trace_ids": [],
        "digital_signature": "auto_signature"
    }
}
