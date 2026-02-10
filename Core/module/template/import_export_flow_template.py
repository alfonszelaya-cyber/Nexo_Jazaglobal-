# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE FLUJO DE IMPORTACIÓN / EXPORTACIÓN
# 10 AÑOS – MULTI PAÍS – MULTI MONEDA – GLOBAL SAFE
# ============================================================

IMPORT_EXPORT_FLOW_TEMPLATE = {
    "flow_metadata": {
        "flow_id": "auto",
        "version": "1.0",
        "country_origin": "auto",
        "country_destination": "auto",
        "currency": "client_choice",
        "status": "DRAFT",  # DRAFT | ACTIVE | COMPLETED | CANCELLED
        "created_at": "auto",
        "updated_at": "auto"
    },

    "parties": {
        "exporter": {
            "name": "",
            "tax_id": "",
            "address": "",
            "contact": ""
        },
        "importer": {
            "name": "",
            "tax_id": "",
            "address": "",
            "contact": ""
        },
        "logistics_provider": {
            "name": "",
            "contact": "",
            "tracking_id": ""
        }
    },

    "goods": [
        {
            "sku": "",
            "description": "",
            "quantity": 0,
            "unit_price": 0.0,
            "currency": "BASE",
            "total_value": 0.0,
            "tax": 0.0,
            "weight_kg": 0.0,
            "volume_m3": 0.0,
            "hazardous": False
        }
    ],

    "flow_steps": [
        "DOCUMENTATION_CHECK",
        "CUSTOMS_CLEARANCE",
        "TRANSPORT",
        "DELIVERY_CONFIRMATION",
        "PAYMENT"
    ],

    "compliance": {
        "zyra_pre_validate": True,
        "country_customs_rules": True,
        "audit_trail_enabled": True,
        "memory_level": "LONG_TERM",
        "predict_risks": True
    },

    "financials": {
        "total_invoice": 0.0,
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
# FIN DE PLANTILLA DE FLUJO DE IMPORTACIÓN / EXPORTACIÓN
# ============================================================