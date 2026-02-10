# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE FLUJO DE PAGO / NÓMINA
# 10 AÑOS – MULTI PAÍS – MULTI MONEDA – GLOBAL SAFE
# ============================================================

PAYROLL_PAYMENT_FLOW_TEMPLATE = {
    "flow_metadata": {
        "flow_id": "auto",
        "version": "1.0",
        "country": "auto",
        "currency": "client_choice",
        "status": "DRAFT",  # DRAFT | ACTIVE | COMPLETED | CANCELLED
        "created_at": "auto",
        "updated_at": "auto"
    },

    "employer": {
        "name": "",
        "tax_id": "",
        "address": "",
        "contact": ""
    },

    "employees": [
        {
            "employee_id": "auto",
            "name": "",
            "tax_id": "",
            "role": "",
            "base_salary": 0.0,
            "allowances": 0.0,
            "deductions": 0.0,
            "currency": "BASE",
            "payment_status": "PENDING"  # PENDING | PARTIAL | PAID
        }
    ],

    "payment_schedule": {
        "period": "MONTHLY",          # WEEKLY | BIWEEKLY | MONTHLY
        "next_payment_date": "auto",
        "method": "TRANSFER",         # TRANSFER | CASH | CRYPTO | MIXED
        "partial_payments_allowed": False
    },

    "compliance": {
        "zyra_pre_validate": True,
        "tax_withholding_rules": True,
        "audit_trail_enabled": True,
        "memory_level": "LONG_TERM",
        "predict_risks": True
    },

    "financials": {
        "total_gross": 0.0,
        "total_tax": 0.0,
        "total_net": 0.0,
        "currency": "client_choice",
        "exchange_rate_reference": "zyra_rate"
    },

    "audit_trail": {
        "linked_documents": [],
        "hash": "auto",
        "immutable": True
    }
}

# ============================================================
# FIN DE PLANTILLA DE FLUJO DE PAGO / NÓMINA GLOBAL
# ============================================================