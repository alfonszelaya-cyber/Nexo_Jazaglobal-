# delivery_confirmation.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# CONFIRMACIÓN DE ENTREGA
# PASIVO | EVENT-DRIVEN

from datetime import datetime, timezone

def confirm_delivery(payload: dict) -> dict:
    """
    Confirma entrega del embarque.
    """
    return {
        "shipment_id": payload.get("shipment_id"),
        "delivered": True,
        "evidence": payload.get("evidence"),  # foto / firma / doc
        "confirmed_at": datetime.now(timezone.utc).isoformat()
    }