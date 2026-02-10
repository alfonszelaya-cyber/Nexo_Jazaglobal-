# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE FLUJO DE PAGO UNIVERSAL
# 10+ AÑOS – MULTI PAÍS – MULTI MONEDA – CORE SAFE
# ============================================================

PAYMENT_FLOW_TEMPLATE = {
    "flow_metadata": {
        "flow_id": "auto",
        "version": "1.0",
        "country": "auto",
        "currency": "client_choice",
        "created_at": "auto",
        "status": "PENDING"  # PENDING | COMPLETED | FAILED | CANCELLED
    },

    "payer": {
        "name": "",
        "tax_id": "",
        "address": "",
        "contact": ""
    },

    "receiver": {
        "name": "",
        "tax_id": "",
        "address": "",
        "contact": "",
        "preferred_currency": "client_choice"
    },

    "payment_items": [
        {
            "reference_id": "",
            "description": "",
            "amount": 0.0,
            "currency": "BASE",
            "method": "TRANSFER",  # TRANSFER | CASH | CARD | CRYPTO | MIXED
            "tax": 0.0,
            "discount": 0.0,
            "total": 0.0,
            "status": "PENDING"  # PENDING | COMPLETED | FAILED
        }
    ],

    "totals": {
        "subtotal": 0.0,
        "tax_total": 0.0,
        "discount_total": 0.0,
        "grand_total": 0.0,
        "currency_display": "client_choice"
    },

    "zyra_supervision": {
        "validate_funds": True,
        "predict_risk": True,
        "audit_trail_enabled": True,
        "memory_level": "LONG_TERM"
    },

    "audit_trail": {
        "linked_documents": [],
        "hash": "auto",
        "immutable": True
    }
}

# ============================================================
# FIN DE PLANTILLA CANÓNICA DE FLUJO DE PAGO
# ============================================================