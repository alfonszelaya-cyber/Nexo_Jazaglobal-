# ============================================================
# ZYRA / NEXO
# AUTH SCHEMA — ENTERPRISE 3.0
# ============================================================

from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


# ============================================================
# LOGIN
# ============================================================

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)


class LoginResponse(BaseModel):
    user: str
    access_token: str
    token_type: str = "bearer"
    expires_in_minutes: int
    issued_at: datetime
    expires_at: datetime


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
    token: str


class TokenValidationResponse(BaseModel):
    access_granted: bool
    validated_at: datetime


# ============================================================
# LOGOUT
# ============================================================

class LogoutRequest(BaseModel):
    email: EmailStr


class LogoutResponse(BaseModel):
    user: str
    status: str
    timestamp: datetime
