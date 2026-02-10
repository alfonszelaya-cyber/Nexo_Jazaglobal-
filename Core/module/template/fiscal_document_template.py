# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE DOCUMENTO FISCAL UNIVERSAL
# 10 AÑOS – MULTI PAÍS – MULTI MONEDA
# ============================================================

FISCAL_DOCUMENT_TEMPLATE = {

    "document_metadata": {
        "document_type": "INVOICE",          # INVOICE | RECEIPT | CREDIT_NOTE
        "version": "1.0",
        "country": "auto",                   # auto | ISO-3166
        "language": "country_default",
        "issue_datetime": "auto",
        "timezone": "country_default"
    },

    "issuer": {
        "legal_name": "",
        "tax_id": "",
        "country": "",
        "address": "",
        "economic_activity": "",
        "authorized_by_zyra": True
    },

    "receiver": {
        "name": "",
        "tax_id": "",
        "country": "",
        "address": "",
        "client_type": "NATURAL",             # NATURAL | LEGAL
        "preferred_currency": "client_choice"
    },

    "items": [
        {
            "sku": "",
            "description": "",
            "quantity": 1,
            "unit_price": 0.0,
            "currency": "BASE",
            "taxable": True,
            "discount": 0.0
        }
    ],

    "totals": {
        "subtotal": "auto",
        "discount_total": "auto",
        "tax_total": "auto",
        "grand_total": "auto",
        "currency_display": "client_choice"
    },

    "taxes": {
        "apply_country_rules": True,
        "tax_schema": "country_default",
        "breakdown_required": True
    },

    "currency": {
        "base_currency": "USD",
        "document_currency": "client_choice",
        "exchange_rate_locked": True,
        "exchange_reference": "zyra_rate"
    },

    "payment_terms": {
        "method": "TRANSFER",                # CASH | CARD | TRANSFER | CRYPTO
        "due_date": "auto",
        "partial_payments_allowed": False
    },

    "compliance": {
        "fiscal_signature_required": True,
        "government_reporting": True,
        "store_min_years": 10,
        "audit_ready": True
    },

    "zyra_controls": {
        "pre_validate": True,
        "post_validate": True,
        "predict_rejection_risk": True,
        "explain_to_user": True
    }
}

# ============================================================
# FIN DE PLANTILLA
# ============================================================