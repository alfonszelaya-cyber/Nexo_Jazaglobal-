# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE REPORTE FINANCIERO UNIVERSAL
# 10 AÑOS – MULTI PAÍS – MULTI MONEDA
# ============================================================

FINANCIAL_REPORT_TEMPLATE = {

    "report_metadata": {
        "report_type": "FINANCIAL",          # FINANCIAL | SALES | TAX | AUDIT
        "version": "1.0",
        "generated_by": "ZYRA",
        "country": "auto",
        "language": "country_default",
        "generated_at": "auto",
        "period": {
            "from": "YYYY-MM-DD",
            "to": "YYYY-MM-DD"
        }
    },

    "entity": {
        "entity_name": "",
        "entity_id": "",
        "entity_type": "COMPANY",            # COMPANY | PERSON | GOVERNMENT
        "country": "",
        "currency_base": "USD"
    },

    "scope": {
        "by_country": False,
        "by_client": False,
        "by_module": False,
        "by_currency": False,
        "filters": []
    },

    "financial_summary": {
        "total_income": 0.0,
        "total_expenses": 0.0,
        "gross_profit": "auto",
        "net_profit": "auto",
        "currency": "base"
    },

    "breakdown": {
        "income_sources": [],
        "expense_categories": [],
        "taxes_collected": [],
        "currency_conversions": []
    },

    "tax_section": {
        "apply_country_rules": True,
        "report_to_government": False,
        "tax_schema": "country_default",
        "compliance_status": "auto"
    },

    "risk_analysis": {
        "enabled": True,
        "zyra_predictive_risk": "auto",
        "anomalies_detected": [],
        "alerts": []
    },

    "audit": {
        "audit_ready": True,
        "traceability_level": "FULL",        # FULL | PARTIAL
        "source_documents": [],
        "immutable_hash": "auto"
    },

    "output": {
        "formats": ["PDF", "JSON"],
        "human_readable": True,
        "explainable_by_zyra": True
    }
}

# ============================================================
# FIN DE PLANTILLA
# ============================================================