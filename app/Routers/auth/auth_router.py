# ============================================================
# ZYRA / NEXO
# AUTH ROUTER — ENTERPRISE 3.0
# ============================================================

from fastapi import APIRouter
from datetime import datetime

from app.Schemas.auth.auth_schema import (
    LoginRequest,
    LoginResponse,
    TokenValidationRequest,
    TokenValidationResponse,
    LogoutRequest,
    LogoutResponse
)

from app.Services.auth.auth_services import AuthServices


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

auth_service = AuthServices()


# ============================================================
# STATUS
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
    result = auth_service.login(payload.model_dump())
    return LoginResponse(**result)


# ============================================================
# VALIDATE TOKEN
# ============================================================

@router.post("/validate", response_model=TokenValidationResponse)
def validate_token(payload: TokenValidationRequest):
    result = auth_service.validate_token(payload.token)
    return TokenValidationResponse(**result)


# ============================================================
# LOGOUT
# ============================================================

@router.post("/logout", response_model=LogoutResponse)
def logout(payload: LogoutRequest):
    result = auth_service.logout(payload.user)
    return LogoutResponse(**result)
