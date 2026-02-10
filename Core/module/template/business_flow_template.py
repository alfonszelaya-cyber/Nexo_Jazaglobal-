# ============================================================
# ZYRA / NEXO
# PLANTILLA CANÓNICA DE FLUJO DE NEGOCIO
# Importación | Venta | Pago
# 10 AÑOS – MULTI PAÍS – MULTI MONEDA – PRODUCCIÓN
# ============================================================

BUSINESS_FLOW_TEMPLATE = {

    "flow_metadata": {
        "flow_id": "auto",
        "flow_type": "IMPORTACION",     # IMPORTACION | VENTA | PAGO | MIXTO
        "version": "1.0",
        "country": "auto",
        "created_by": "ZYRA",
        "created_at": "auto",
        "updated_at": "auto",
        "status": "DRAFT"               # DRAFT | ACTIVE | CLOSED | CANCELLED
    },

    "participants": {
        "buyer": {
            "name": "",
            "tax_id": "",
            "address": "",
            "contact": ""
        },
        "seller": {
            "name": "",
            "tax_id": "",
            "address": "",
            "contact": ""
        },
        "provider": {
            "name": "",
            "tax_id": "",
            "address": "",
            "contact": ""
        },
        "logistics": {
            "company": "",
            "tracking_id": "",
            "method": ""                 # LAND | AIR | SEA
        },
        "government": {
            "authority": "",
            "reference_id": ""
        }
    },

    "commercial_terms": {
        "currency_base": "USD",
        "payment_method": "TRANSFER",   # TRANSFER | CASH | CARD | CRYPTO | MIXED
        "incoterm": "EXW",               # EXW | FOB | CIF | DDP
        "contract_reference": None
    },

    "steps": [
        {
            "step_order": 1,
            "step_name": "ORIGIN_VALIDATION",
            "module_executor": "RADAR_VIP",
            "requires_approval": True,
            "risk_level": "auto"
        },
        {
            "step_order": 2,
            "step_name": "COST_CALCULATION",
            "module_executor": "FINANZAS",
            "requires_approval": True,
            "risk_level": "auto"
        },
        {
            "step_order": 3,
            "step_name": "PAYMENT_EXECUTION",
            "module_executor": "PAGOS",
            "requires_approval": True,
            "risk_level": "auto"
        },
        {
            "step_order": 4,
            "step_name": "LOGISTICS_EXECUTION",
            "module_executor": "LOGISTICA",
            "requires_approval": False,
            "risk_level": "auto"
        },
        {
            "step_order": 5,
            "step_name": "FINAL_SETTLEMENT",
            "module_executor": "CONTABILIDAD",
            "requires_approval": True,
            "risk_level": "auto"
        }
    ],

    "zyra_supervision": {
        "predict_risk_before_each_step": True,
        "auto_block_on_high_risk": True,
        "memory_level": "LONG_TERM",     # SHORT_TERM | LONG_TERM
        "explain_decisions": True
    },

    "audit_trail": {
        "enabled": True,
        "immutable": True,
        "linked_documents": [],
        "hash": "auto"
    }
}

# ============================================================
# FIN DE PLANTILLA CANÓNICA DE FLUJO DE NEGOCIO
# ============================================================