# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE FLUJO DE VENTA / COMERCIALIZACIÓN
# 10 AÑOS – MULTI PAÍS – MULTI MONEDA – GLOBAL SAFE
# ============================================================

SALES_FLOW_TEMPLATE = {
    "flow_metadata": {
        "flow_id": "auto",
        "version": "1.0",
        "country": "auto",
        "currency": "client_choice",
        "status": "DRAFT",           # DRAFT | IN_PROGRESS | COMPLETED | CANCELLED
        "created_at": "auto",
        "updated_at": "auto"
    },

    "seller": {
        "name": "",
        "tax_id": "",
        "address": "",
        "contact": ""
    },

    "buyer": {
        "name": "",
        "tax_id": "",
        "address": "",
        "contact": "",
        "client_type": "NATURAL",     # NATURAL | LEGAL
        "preferred_currency": "client_choice"
    },

    "products": [
        {
            "sku": "",
            "description": "",
            "quantity": 1,
            "unit_price": 0.0,
            "currency": "BASE",
            "taxable": True,
            "discount": 0.0,
            "total_price": 0.0
        }
    ],

    "payment_terms": {
        "method": "TRANSFER",          # CASH | CARD | TRANSFER | CRYPTO
        "due_date": "auto",
        "partial_payments_allowed": False,
        "paid": False
    },

    "logistics": {
        "delivery_method": "LAND",     # LAND | AIR | SEA
        "dispatch_date": "auto",
        "arrival_date": "auto",
        "tracking_id": "auto"
    },

    "compliance": {
        "zyra_pre_validate": True,
        "fiscal_rules_country": True,
        "audit_trail_enabled": True,
        "memory_level": "LONG_TERM",
        "predict_risks": True
    },

    "financials": {
        "subtotal": 0.0,
        "tax_total": 0.0,
        "discount_total": 0.0,
        "grand_total": 0.0,
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
# FIN DE PLANTILLA DE FLUJO DE VENTA / COMERCIALIZACIÓN
# ============================================================