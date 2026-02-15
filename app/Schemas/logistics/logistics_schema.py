# ============================================================
# ZYRA / NEXO
# LOGISTICS SCHEMA — ENTERPRISE 3.0
# Operations & Shipment Management Layer
# ============================================================

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ============================================================
# CREATE SHIPMENT
# ============================================================

class CreateShipmentRequest(BaseModel):
    shipment_type: str  # IMPORT | EXPORT | LOCAL
    origin_country: str
    destination_country: str
    carrier: Optional[str]
    tracking_number: Optional[str]


class ShipmentResponse(BaseModel):
    shipment_id: str
    shipment_type: str
    status: str  # CREATED | IN_TRANSIT | DELIVERED | CANCELLED
    created_at: datetime


# ============================================================
# UPDATE SHIPMENT STATUS
# ============================================================

class UpdateShipmentStatus(BaseModel):
    shipment_id: str
    new_status: str
    updated_at: datetime
