
# ============================================================
# ZYRA / NEXO
# AUTH ROUTER — ENTERPRISE 3.0
# Authentication & Authorization Layer
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ===============================
# IMPORT SCHEMAS
# ===============================

from app.Schemas.auth.auth_schema import (
    LoginRequest,
    LoginResponse,
    TokenValidationRequest,
    TokenValidationResponse,
    LogoutRequest,
    LogoutResponse
)

# ===============================
# IMPORT SERVICE
# ===============================

from app.Services.auth.auth_services import AuthServices

# ===============================
# ROUTER
# ===============================

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

auth_service = AuthService()

# ============================================================
# AUTH STATUS
# ============================================================

@router.get("/status")
def auth_status():
    return {
        "module": "ZYRA_AUTH_ENGINE",
        "status": "active",
        "version": "3.0.0",
        "timestamp": datetime.utcnow()
    }

# ============================================================
# LOGIN
# ============================================================

@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    try:
        return auth_service.login(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ============================================================
# VALIDATE TOKEN
# ============================================================

@router.post("/validate", response_model=TokenValidationResponse)
def validate_token(payload: TokenValidationRequest):
    try:
        return auth_service.validate_token(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ============================================================
# LOGOUT
# ============================================================

@router.post("/logout", response_model=LogoutResponse)
def logout(payload: LogoutRequest):
    try:
        return auth_service.logout(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
