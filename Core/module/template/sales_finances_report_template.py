# ============================================================
# ZYRA / NEXO
# SALES FINANCE REPORT TEMPLATE — ENTERPRISE 3.0
# ============================================================

SALES_FINANCE_REPORT_TEMPLATE = {
    "report_metadata": {
        "report_id": "auto_uuid",
        "report_type": "SALES_FINANCE",
        "schema_version": "3.0",
        "generated_by": "ZYRA_ENGINE",
        "generated_at": "auto_utc",
        "country": "auto",
        "base_currency": "USD",
        "presentation_currency": "client_choice",
        "status": "DRAFT",
        "integrity_hash": "auto_hash"
    },
    "company_profile": {
        "company_id": "auto",
        "legal_name": "",
        "tax_id": "",
        "industry_sector": "",
        "operational_region": "",
        "compliance_profile": "STRICT"
    },
    "reporting_period": {
        "start_date": "auto",
        "end_date": "auto",
        "fiscal_year": "auto"
    },
    "sales_metrics": {
        "total_transactions": 0,
        "units_sold_total": 0,
        "gross_revenue": 0.0,
        "discounts_total": 0.0,
        "returns_total": 0.0,
        "net_revenue": 0.0,
        "currency": "base_currency"
    },
    "sales_breakdown": [
        {
            "product_id": "",
            "sku": "",
            "description": "",
            "category": "",
            "units_sold": 0,
            "unit_price": 0.0,
            "gross_sales": 0.0,
            "tax_amount": 0.0,
            "discount_applied": 0.0,
            "net_sales": 0.0,
            "currency": "BASE",
            "linked_invoice_ids": [],
            "risk_flag": False
        }
    ],
    "tax_structure": {
        "tax_model": "MULTI_LAYER",
        "total_tax_collected": 0.0,
        "tax_breakdown": [
            {
                "tax_type": "VAT",
                "rate": 0.0,
                "amount": 0.0
            }
        ]
    },
    "intelligence_layer": {
        "top_selling_products": [],
        "regional_performance": [],
        "customer_segment_analysis": [],
        "revenue_growth_rate": 0.0,
        "risk_score": 0.0
    },
    "compliance_controls": {
        "cross_check_with_ledger": True,
        "cross_check_with_tax_module": True,
        "audit_ready": True,
        "immutable": True
    },
    "audit_trail": {
        "linked_documents": [],
        "event_trace_ids": [],
        "digital_signature": "auto_signature"
    }
}
