# ============================================================
# ZYRA / NEXO
# COMPLIANCE ROUTER — ENTERPRISE 3.0
# Regulatory & Risk Control Layer
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.compliance.compliance_schema import (
    ComplianceStatusResponse,
    EntityValidationRequest,
    EntityValidationResponse,
    RiskCheckRequest,
    RiskCheckResponse,
    ComplianceEventRequest,
    ComplianceEventResponse
)

# ============================
# IMPORT SERVICE (FIXED PATH)
# ============================

from app.Services.compliance.compliance_services import ComplianceService


router = APIRouter(
    prefix="/compliance",
    tags=["Compliance"]
)

compliance_service = ComplianceService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=ComplianceStatusResponse)
def compliance_status():
    return ComplianceStatusResponse(
        module="ZYRA_COMPLIANCE_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# VALIDATE ENTITY
# ============================================================

@router.post("/validate-entity", response_model=EntityValidationResponse)
def validate_entity(payload: EntityValidationRequest):
    try:
        return compliance_service.validate_entity(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# CHECK RISK
# ============================================================

@router.post("/risk-check", response_model=RiskCheckResponse)
def risk_check(payload: RiskCheckRequest):
    try:
        return compliance_service.check_risk(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# REGISTER COMPLIANCE EVENT
# ============================================================

@router.post("/register-event", response_model=ComplianceEventResponse)
def register_compliance_event(payload: ComplianceEventRequest):
    try:
        return compliance_service.register_event(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
