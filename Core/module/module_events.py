# ============================================================
# NEXO / ZYRA — CORE MODULE EVENTS ENGINE
# Central Event Registry for Support Modules
# Passive | Canonical | Enterprise Ready
# ============================================================

from datetime import datetime, timezone
import uuid

# ============================================================
# EVENT CATALOG
# ============================================================

MODULE_EVENTS = {
    "SHIPMENT_CREATED",
    "SHIPMENT_UPDATED",
    "TRACKING_UPDATED",
    "CUSTOMS_CLEARED",
    "DELIVERY_CONFIRMED",
    "LOGISTICS_ALERT",

    "OPERATION_EXECUTED",
    "OPERATION_UPDATED",
    "OPERATION_CANCELLED",

    "NOTIFICATION_SENT",
    "NOTIFICATION_FAILED",

    "DOCUMENT_UPLOADED",
    "DOCUMENT_ARCHIVED"
}

# ============================================================
# UTIL
# ============================================================

def _now():
    return datetime.now(timezone.utc).isoformat()

# ============================================================
# GENERIC EVENT REGISTRAR
# ============================================================

def register_event(event_type: str, payload: dict) -> dict:
    if event_type not in MODULE_EVENTS:
        return {
            "status": "ERROR",
            "message": "Invalid module event",
            "event_type": event_type
        }

    return {
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "payload": payload,
        "timestamp": _now(),
        "status": "REGISTERED"
    }

# ============================================================
# SPECIFIC COMPATIBILITY FUNCTIONS
# ============================================================

def register_operation_event(payload: dict) -> dict:
    return register_event("OPERATION_EXECUTED", payload)


def register_notification_event(payload: dict) -> dict:
    return register_event("NOTIFICATION_SENT", payload)


def register_shipment_event(payload: dict) -> dict:
    return register_event("SHIPMENT_CREATED", payload)


def register_document_event(payload: dict) -> dict:
    return register_event("DOCUMENT_UPLOADED", payload)
