# shipment_engine.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# ENGINE DE EMBARQUES ASIA → DESTINO
# EVENT-DRIVEN | PASIVO | ENTERPRISE READY

from datetime import datetime, timezone
import uuid

# ============================================================
# UTILIDAD TIEMPO
# ============================================================

def _now():
    return datetime.now(timezone.utc).isoformat()

# ============================================================
# CREAR EMBARQUE BASE (NO TOCAR)
# ============================================================

def create_shipment(payload: dict) -> dict:
    """
    Crea un embarque lógico.
    El evento real lo emite el router del módulo.
    """
    return {
        "shipment_id": payload.get("shipment_id"),
        "origen": payload.get("origen"),
        "destino": payload.get("destino"),
        "created_at": _now(),
        "status": "CREATED"
    }

# ============================================================
# REGISTER SHIPMENT IN CORE (COMPATIBLE CON ROUTERS)
# ============================================================

def register_shipment_in_core(payload: dict) -> dict:
    shipment_id = payload.get("shipment_id") or str(uuid.uuid4())

    return {
        "shipment_id": shipment_id,
        "shipment_type": payload.get("shipment_type", "ASIA"),
        "origen": payload.get("origen"),
        "destino": payload.get("destino"),
        "carrier": payload.get("carrier"),
        "tracking_number": payload.get("tracking_number"),
        "status": "CREATED",
        "created_at": _now(),
        "history": [
            {
                "status": "CREATED",
                "timestamp": _now()
            }
        ]
    }

# ============================================================
# UPDATE SHIPMENT STATUS
# ============================================================

def update_shipment_status_in_core(
    shipment_id: str,
    new_status: str
) -> dict:

    return {
        "shipment_id": shipment_id,
        "new_status": new_status,
        "updated_at": _now()
    }

# ============================================================
# TRACK SHIPMENT
# ============================================================

def track_shipment_in_core(shipment_id: str) -> dict:
    return {
        "shipment_id": shipment_id,
        "status": "IN_TRANSIT",
        "last_update": _now()
    }

# ============================================================
# CANCEL SHIPMENT
# ============================================================

def cancel_shipment_in_core(shipment_id: str) -> dict:
    return {
        "shipment_id": shipment_id,
        "status": "CANCELLED",
        "cancelled_at": _now()
    }
