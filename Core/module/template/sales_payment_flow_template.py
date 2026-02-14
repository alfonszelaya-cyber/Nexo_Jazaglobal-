# ============================================================
# ZYRA / NEXO
# SALES PAYMENT FLOW TEMPLATE
# VERSION 2.0 – ENTERPRISE GLOBAL READY
# ============================================================

SALES_PAYMENT_FLOW_TEMPLATE = {
    "meta": {
        "flow_id": "auto_uuid",
        "version": "2.0",
        "environment": "PRODUCTION",  # DEV | STAGING | PRODUCTION
        "region": "auto",
        "country": "auto",
        "base_currency": "USD",
        "client_currency": "auto",
        "created_at_utc": "auto",
        "updated_at_utc": "auto",
        "created_by": "system_or_user_id"
    },

    "actors": {
        "seller": {
            "entity_id": "",
            "legal_name": "",
            "tax_id": "",
            "country": "",
            "address": "",
            "contact_email": ""
        },
        "buyer": {
            "entity_id": "",
            "legal_name": "",
            "tax_id": "",
            "country": "",
            "client_type": "NATURAL",  # NATURAL | LEGAL
            "risk_profile": "LOW",     # LOW | MEDIUM | HIGH
            "preferred_currency": ""
        }
    },

    "order": {
        "order_id": "",
        "order_status": "DRAFT",  # DRAFT | CONFIRMED | CANCELLED
        "items": [],
        "notes": "",
        "source_channel": "WEB"  # WEB | POS | API | MOBILE
    },

    "payment": {
        "payment_id": "",
        "method": "TRANSFER",  # CASH | CARD | TRANSFER | CRYPTO
        "processor": "",
        "transaction_reference": "",
        "payment_status": "PENDING",  # PENDING | PARTIAL | PAID | FAILED
        "paid_amount": 0.0,
        "due_date": "auto",
        "installments": []
    },

    "financial_summary": {
        "subtotal": 0.0,
        "tax_total": 0.0,
        "discount_total": 0.0,
        "grand_total": 0.0,
        "exchange_rate": 1.0,
        "currency": "USD"
    },

    "compliance": {
        "tax_validated": False,
        "fraud_checked": False,
        "kyc_verified": False,
        "country_rules_applied": True,
        "audit_enabled": True
    },

    "audit": {
        "event_log": [],
        "immutable_hash": "auto_hash",
        "archived": False
    }
}
