# ============================================================
# ZYRA / NEXO
# PAYROLL PAYMENT FLOW TEMPLATE
# VERSION 2.0 – ENTERPRISE GLOBAL READY
# ============================================================

PAYROLL_PAYMENT_FLOW_TEMPLATE = {
    "meta": {
        "flow_id": "auto_uuid",
        "version": "2.0",
        "environment": "PRODUCTION",   # DEV | STAGING | PRODUCTION
        "country": "auto",
        "region": "auto",
        "base_currency": "USD",
        "payroll_currency": "auto",
        "created_at_utc": "auto",
        "updated_at_utc": "auto",
        "created_by": "system_or_user_id"
    },

    "employer": {
        "entity_id": "",
        "legal_name": "",
        "tax_id": "",
        "country": "",
        "industry": "",
        "compliance_profile": "STANDARD"  # STANDARD | HIGH_REGULATION
    },

    "payroll_cycle": {
        "cycle_id": "",
        "period_type": "MONTHLY",     # WEEKLY | BIWEEKLY | MONTHLY
        "period_start": "auto",
        "period_end": "auto",
        "approval_status": "DRAFT",   # DRAFT | APPROVED | EXECUTED
        "processed_by": ""
    },

    "employees": [
        {
            "employee_id": "",
            "employment_type": "FULL_TIME",  # FULL_TIME | PART_TIME | CONTRACTOR
            "risk_profile": "LOW",
            "compensation": {
                "base_salary": 0.0,
                "bonuses": 0.0,
                "allowances": 0.0,
                "overtime": 0.0
            },
            "deductions": {
                "tax": 0.0,
                "social_security": 0.0,
                "other": 0.0
            },
            "net_pay": 0.0,
            "currency": "BASE",
            "payment_status": "PENDING"  # PENDING | PARTIAL | PAID | FAILED
        }
    ],

    "payment_execution": {
        "method": "TRANSFER",      # TRANSFER | CASH | CRYPTO | MIXED
        "bank_reference": "",
        "batch_id": "",
        "execution_date": "auto",
        "total_processed": 0.0
    },

    "financial_summary": {
        "total_gross": 0.0,
        "total_deductions": 0.0,
        "total_net": 0.0,
        "exchange_rate": 1.0,
        "currency": "USD"
    },

    "compliance": {
        "tax_withholding_validated": False,
        "labor_law_checked": False,
        "country_rules_applied": True,
        "fraud_checked": False,
        "audit_enabled": True
    },

    "intelligence": {
        "payroll_risk_score": 0,
        "anomaly_detected": False,
        "flags": []
    },

    "audit": {
        "event_log": [],
        "immutable_hash": "auto_hash",
        "archived": False
    }
}
