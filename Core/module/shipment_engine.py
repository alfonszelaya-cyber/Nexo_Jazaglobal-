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
# CREAR EMBARQUE BASE
# ============================================================

def create_shipment(payload: dict) -> dict:
    return {
        "shipment_id": payload.get("shipment_id") or str(uuid.uuid4()),
        "origen": payload.get("origen"),
        "destino": payload.get("destino"),
        "created_at": _now(),
        "status": "CREATED"
    }

# ============================================================
# REGISTER
# ============================================================

def register_shipment_in_core(payload: dict) -> dict:
    return create_shipment(payload)

# Alias en español (por si el router usa este nombre)
def registrar_envio_en_core(payload: dict) -> dict:
    return register_shipment_in_core(payload)

# ============================================================
# UPDATE STATUS
# ============================================================

def update_shipment_status_in_core(shipment_id: str, new_status: str) -> dict:
    return {
        "shipment_id": shipment_id,
        "status": new_status,
        "updated_at": _now()
    }

# Alias español
def actualizar_estado_envio_en_core(shipment_id: str, new_status: str) -> dict:
    return update_shipment_status_in_core(shipment_id, new_status)

# ============================================================
# TRACK
# ============================================================

def track_shipment_in_core(shipment_id: str) -> dict:
    return {
        "shipment_id": shipment_id,
        "status": "IN_TRANSIT",
        "last_update": _now()
    }

# Alias
def rastrear_envio_en_core(shipment_id: str) -> dict:
    return track_shipment_in_core(shipment_id)

# ============================================================
# CONFIRM DELIVERY
# ============================================================

def confirm_delivery_in_core(shipment_id: str) -> dict:
    return {
        "shipment_id": shipment_id,
        "status": "DELIVERED",
        "delivered_at": _now()
    }

# Alias español
def confirmar_entrega_en_core(shipment_id: str) -> dict:
    return confirm_delivery_in_core(shipment_id)

# ============================================================
# CANCEL
# ============================================================

def cancel_shipment_in_core(shipment_id: str) -> dict:
    return {
        "shipment_id": shipment_id,
        "status": "CANCELLED",
        "cancelled_at": _now()
    }

# Alias español
def cancelar_envio_en_core(shipment_id: str) -> dict:
    return cancel_shipment_in_core(shipment_id)
