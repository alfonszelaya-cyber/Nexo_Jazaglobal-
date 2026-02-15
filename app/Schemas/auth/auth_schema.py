# ============================================================
# ZYRA / NEXO
# AUTH SCHEMA — ENTERPRISE 3.0
# Authentication & Authorization Contracts
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

class TokenValidationResponse(BaseModel):
    valid: bool
    user: Optional[str]
    roles: Optional[List[str]]
    checked_at: datetime
