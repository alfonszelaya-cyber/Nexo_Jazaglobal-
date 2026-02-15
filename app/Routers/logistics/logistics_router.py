# ============================================================
# ZYRA / NEXO
# LOGISTICS ROUTER — ENTERPRISE 3.0
# Shipment & Delivery Control Layer
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.logistics_schema import (
    LogisticsStatusResponse,
    ShipmentCreateRequest,
    ShipmentCreateResponse,
    ShipmentStatusUpdateRequest,
    ShipmentStatusUpdateResponse,
    ShipmentTrackRequest,
    ShipmentTrackResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.logistics_services import LogisticsService


router = APIRouter(
    prefix="/logistics",
    tags=["Logistics"]
)

logistics_service = LogisticsService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=LogisticsStatusResponse)
def logistics_status():
    return LogisticsStatusResponse(
        module="ZYRA_LOGISTICS_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# CREATE SHIPMENT
# ============================================================

@router.post("/create-shipment", response_model=ShipmentCreateResponse)
def create_shipment(payload: ShipmentCreateRequest):
    try:
        return logistics_service.create_shipment(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# UPDATE SHIPMENT STATUS
# ============================================================

@router.post("/update-status", response_model=ShipmentStatusUpdateResponse)
def update_shipment_status(payload: ShipmentStatusUpdateRequest):
    return logistics_service.update_status(payload)


# ============================================================
# TRACK SHIPMENT
# ============================================================

@router.post("/track", response_model=ShipmentTrackResponse)
def track_shipment(payload: ShipmentTrackRequest):
    return logistics_service.track_shipment(payload)
