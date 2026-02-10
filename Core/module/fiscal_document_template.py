# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE DOCUMENTO FISCAL
# Factura | Recibo | Contrato
# 10 AÑOS – MULTI PAÍS – MULTI MONEDA
# ============================================================

FISCAL_DOCUMENT_TEMPLATE = {

    "document_metadata": {
        "doc_id": "auto",
        "doc_type": "FACTURA",       # FACTURA | RECIBO | CONTRATO
        "version": "1.0",
        "country": "auto",
        "created_by": "ZYRA",
        "created_at": "auto",
        "status": "DRAFT"            # DRAFT | FINAL | CANCELLED
    },

    "issuer": {
        "name": "",
        "tax_id": "",
        "address": "",
        "contact": ""
    },

    "receiver": {
        "name": "",
        "tax_id": "",
        "address": "",
        "contact": ""
    },

    "line_items": [
        {
            "item_id": "auto",
            "description": "",
            "quantity": 0,
            "unit_price": 0.0,
            "currency": "USD",
            "total_price": 0.0,
            "tax": 0.0
        }
    ],

    "totals": {
        "subtotal": 0.0,
        "tax_total": 0.0,
        "grand_total": 0.0,
        "currency": "USD"
    },

    "payment_info": {
        "method": "TRANSFER",       # TRANSFER | CASH | CRYPTO | MIXED
        "due_date": "auto",
        "paid": False
    },

    "zyra_supervision": {
        "check_compliance": True,
        "auto_flag_errors": True,
        "memory_level": "LONG_TERM",
        "audit_trail_enabled": True
    },

    "audit_trail": {
        "linked_flows": [],
        "hash": "auto",
        "immutable": True
    }
}

# ============================================================
# FIN DE PLANTILLA
# ============================================================