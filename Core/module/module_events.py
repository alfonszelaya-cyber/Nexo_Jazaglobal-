# module_events.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# EVENTOS PROPIOS DEL MÓDULO
# PASIVO | CANÓNICO

from datetime import datetime, timezone
import uuid

MODULE_EVENTS = {
    "SHIPMENT_CREATED",
    "SHIPMENT_UPDATED",
    "TRACKING_UPDATED",
    "CUSTOMS_CLEARED",
    "DELIVERY_CONFIRMED",
    "LOGISTICS_ALERT"
}

# ============================================================
# INTERNAL TIME
# ============================================================

def _now():
    return datetime.now(timezone.utc).isoformat()

# ============================================================
# GENERIC MODULE EVENT
# ============================================================

def register_module_event(event_type: str, payload: dict) -> dict:
    if event_type not in MODULE_EVENTS:
        return {
            "status": "ERROR",
            "message": f"Invalid event type: {event_type}"
        }

    return {
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "payload": payload,
        "registered_at": _now(),
        "status": "REGISTERED"
    }

# ============================================================
# NOTIFICATION EVENT (PARA ROUTERS)
# ============================================================

def register_notification_event(payload: dict) -> dict:
    return {
        "event_id": str(uuid.uuid4()),
        "event_type": "LOGISTICS_ALERT",
        "payload": payload,
        "registered_at": _now(),
        "status": "REGISTERED"
    }
