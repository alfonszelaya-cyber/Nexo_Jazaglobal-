# ============================================================
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
    user: str


class LogoutResponse(BaseModel):
    user: str
    status: str
    timestamp: datetime
