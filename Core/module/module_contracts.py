# module_contracts.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# CONTRATOS CANÓNICOS DEL MÓDULO
# INMUTABLE | SIN LÓGICA

MODULE_CONTRACT = {
    "module_name": "LOGISTICA_ASIA",
    "scope": "OPERACIONES",
    "versioned": True,
    "event_driven": True,
    "requires": [
        "EVENT_ROUTER",
        "LEDGER",
        "AUDIT"
    ],
    "emits_events": [
        "SHIPMENT_CREATED",
        "SHIPMENT_UPDATED",
        "CUSTOMS_CLEARED",
        "DELIVERY_CONFIRMED",
        "LOGISTICS_ALERT"
    ],
    "states": [
        "INIT",
        "IN_TRANSIT",
        "CUSTOMS",
        "DELIVERED",
        "ERROR",
        "SAFE_MODE"
    ]
}