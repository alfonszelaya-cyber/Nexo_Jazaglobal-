# ============================================================
# ZYRA / NEXO
# INTEGRATIONS ROUTER — ENTERPRISE 3.0
# External Systems & API Connectors
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.integrations.integrations_schema import (
    IntegrationStatusResponse,
    IntegrationRegisterRequest,
    IntegrationRegisterResponse,
    IntegrationTestRequest,
    IntegrationTestResponse,
    IntegrationSyncRequest,
    IntegrationSyncResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.integrations.integrations_services import IntegrationsService


router = APIRouter(
    prefix="/integrations",
    tags=["Integrations"]
)

integrations_service = IntegrationsService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=IntegrationStatusResponse)
def integrations_status():
    return IntegrationStatusResponse(
        module="ZYRA_INTEGRATIONS_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# REGISTER INTEGRATION
# ============================================================

@router.post("/register", response_model=IntegrationRegisterResponse)
def register_integration(payload: IntegrationRegisterRequest):
    try:
        return integrations_service.register_integration(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# TEST CONNECTION
# ============================================================

@router.post("/test-connection", response_model=IntegrationTestResponse)
def test_connection(payload: IntegrationTestRequest):
    return integrations_service.test_connection(payload)


# ============================================================
# SYNC DATA
# ============================================================

@router.post("/sync", response_model=IntegrationSyncResponse)
def sync_data(payload: IntegrationSyncRequest):
    return integrations_service.sync_data(payload)
