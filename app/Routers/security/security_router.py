# ============================================================
# ZYRA / NEXO
# SECURITY ROUTER — ENTERPRISE 3.0
# Security & Protection Layer
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.security_schema import (
    SecurityStatusResponse,
    GenerateApiKeyResponse,
    HashRequest,
    HashResponse,
    ValidateAccessRequest,
    ValidateAccessResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.security_services import SecurityService


router = APIRouter(
    prefix="/security",
    tags=["Security"]
)

security_service = SecurityService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=SecurityStatusResponse)
def security_status():
    return SecurityStatusResponse(
        module="ZYRA_SECURITY_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# GENERATE API KEY
# ============================================================

@router.get("/generate-api-key", response_model=GenerateApiKeyResponse)
def generate_api_key():
    return security_service.generate_api_key()


# ============================================================
# HASH DATA
# ============================================================

@router.post("/hash", response_model=HashResponse)
def hash_data(payload: HashRequest):
    try:
        return security_service.hash_data(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# VALIDATE ACCESS
# ============================================================

@router.post("/validate-access", response_model=ValidateAccessResponse)
def validate_access(payload: ValidateAccessRequest):
    return security_service.validate_access(payload)
