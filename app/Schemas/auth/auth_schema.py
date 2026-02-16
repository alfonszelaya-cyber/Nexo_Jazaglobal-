# ============================================================
# ZYRA / NEXO
# AUTH SCHEMA — ENTERPRISE 3.0
# Authentication & Authorization Contracts
# File: app/Schemas/auth/auth_schema.py
# ============================================================

from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


# ============================================================
# LOGIN
# ============================================================

class LoginRequest(BaseModel):
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=6)


class LoginResponse(BaseModel):
    user: str
    access_token: str
    token_type: str = "bearer"
    expires_in_minutes: int
    issued_at: datetime


# ============================================================
# REGISTER
# ============================================================

class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)


class RegisterResponse(BaseModel):
    user_id: str
    username: str
    created_at: datetime
    status: str


# ============================================================
# TOKEN VALIDATION
# ============================================================

class TokenValidationRequest(BaseModel):
    token: str = Field(..., description="JWT or access token to validate")


class TokenValidationResponse(BaseModel):
    valid: bool
    user: Optional[str] = None
    roles: Optional[List[str]] = None
    checked_at: datetime


# ============================================================
# LOGOUT
# ============================================================

class LogoutRequest(BaseModel):
    user: str


class LogoutResponse(BaseModel):
    status: str
    timestamp: datetime
