# ============================================================
# ZYRA / NEXO
# AUDIT ROUTER — ENTERPRISE 3.0
# Conectado a Schemas + Services + Core
# ============================================================

from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime

# ===============================
# IMPORT SCHEMAS
# ===============================

from app.Schemas.audit.audit_schema import (
    AuditStatusResponse,
    AuditRegisterRequest,
    AuditRegisterResponse,
    AuditTraceRequest,
    AuditTraceResponse,
    AuditListResponse
)

# ===============================
# IMPORT SERVICE
# ===============================

from app.Services.audit.audit_services import AuditService


router = APIRouter(
    prefix="/audit",
    tags=["Audit"]
)


# ===============================
# DEPENDENCY
# ===============================

def get_service():
    return AuditService()


# ============================================================
# AUDIT STATUS
# ============================================================

@router.get("/status", response_model=AuditStatusResponse)
def audit_status():
    return AuditStatusResponse(
        module="ZYRA_AUDIT_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# REGISTER AUDIT EVENT
# ============================================================

@router.post("/register", response_model=AuditRegisterResponse)
def register_audit_event(
    payload: AuditRegisterRequest,
    service: AuditService = Depends(get_service)
):
    try:
        return service.register_event(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# GET AUDIT TRACE
# ============================================================

@router.post("/trace", response_model=AuditTraceResponse)
def get_audit_trace(
    payload: AuditTraceRequest,
    service: AuditService = Depends(get_service)
):
    try:
        return service.trace(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# LIST AUDIT EVENTS
# ============================================================

@router.get("/events", response_model=AuditListResponse)
def list_audit_events(
    service: AuditService = Depends(get_service)
):
    try:
        return service.list_events()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
