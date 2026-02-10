# module_validators.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# VALIDADORES DEL MÓDULO
# SIN AUTOEJECUCIÓN | USADOS POR HANDLERS

def validate_shipment_payload(payload: dict) -> bool:
    required = ["shipment_id", "origen", "destino"]
    return all(k in payload for k in required)

def validate_tracking_update(payload: dict) -> bool:
    required = ["shipment_id", "status"]
    return all(k in payload for k in required)

def validate_customs_payload(payload: dict) -> bool:
    required = ["shipment_id", "aduana", "documentos"]
    return all(k in payload for k in required)