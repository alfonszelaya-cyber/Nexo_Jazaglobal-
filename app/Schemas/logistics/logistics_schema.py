# ============================================================
# ZYRA / NEXO
# LOGISTICS SCHEMA — ENTERPRISE 3.0
# Operations & Shipment Management Layer
# File: app/Schemas/logistics/logistics_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class LogisticsStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# CREATE SHIPMENT
# ============================================================

class ShipmentCreateRequest(BaseModel):
    shipment_type: str = Field(..., description="IMPORT | EXPORT | LOCAL")
    origin_country: str
    destination_country: str
    carrier: Optional[str] = None
    tracking_number: Optional[str] = None


class ShipmentCreateResponse(BaseModel):
    shipment_id: str
    shipment_type: str
    origin_country: str
    destination_country: str
    carrier: Optional[str] = None
    tracking_number: Optional[str] = None
    status: str
    created_at: datetime


# ============================================================
# UPDATE SHIPMENT STATUS
# ============================================================

class ShipmentStatusUpdateRequest(BaseModel):
    shipment_id: str
    new_status: str


class ShipmentStatusUpdateResponse(BaseModel):
    shipment_id: str
    previous_status: str
    new_status: str
    updated_at: datetime


# ============================================================
# TRACK SHIPMENT
# ============================================================

class ShipmentTrackRequest(BaseModel):
    shipment_id: str


class ShipmentTrackResponse(BaseModel):
    shipment_id: str
    current_status: str
    last_update: datetime
