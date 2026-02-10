# shipment_engine.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# ENGINE DE EMBARQUES ASIA → DESTINO
# EVENT-DRIVEN | PASIVO

from datetime import datetime, timezone

def create_shipment(payload: dict) -> dict:
    """
    Crea un embarque lógico.
    El evento real lo emite el router del módulo.
    """
    return {
        "shipment_id": payload.get("shipment_id"),
        "origen": payload.get("origen"),
        "destino": payload.get("destino"),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "CREATED"
    }