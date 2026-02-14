# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE FLUJO DE VENTA / COBRO
# 10 AÑOS – MULTI PAÍS – MULTI MONEDA – GLOBAL SAFE
# ============================================================

SALES_PAYMENT_FLOW_TEMPLATE = {
    "flow_metadata": {
        "flow_id": "auto",
        "version": "1.0",
        "country": "auto",
        "currency": "client_choice",
        "status": "DRAFT",  # DRAFT | ACTIVE | COMPLETED | CANCELLED
        "created_at": "auto",
        "updated_at": "auto"
    },

    "parties": {
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
            "preferred_currency": "client_choice"
        },
        "payment_processor": {
            "name": "",
            "contact": "",
            "transaction_id": ""
        }
    },

    "products_services": [
        {
            "sku": "",
            "description": "",
            "quantity": 0,
            "unit_price": 0.0,
            "currency": "BASE",
            "total_value": 0.0,
            "tax": 0.0,
            "discount": 0.0
        }
    ],

    "flow_steps": [
        "ORDER_PLACEMENT",
        "INVOICE_ISSUANCE",
        "PAYMENT_COLLECTION",
        "DELIVERY_CONFIRMATION",
        "AFTER_SALES_SERVICE"
    ],

    "compliance": {
        "zyra_pre_validate": True,
        "country_tax_rules": True,
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
        "exchange_rate_reference": "zyra_rate",
        "payment_status": "PENDING"  # PENDING | PARTIAL | PAID
    },

    "audit_trail": {
        "linked_documents": [],
        "hash": "auto",
        "immutable": True
    }
}

# ============================================================
# FIN DE PLANTILLA DE FLUJO DE VENTA / COBRO GLOBAL
# ============================================================