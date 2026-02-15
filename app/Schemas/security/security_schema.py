# ============================================================
# ZYRA / NEXO
# SECURITY SCHEMA — ENTERPRISE 3.0
# Authentication & Authorization Layer
# ============================================================

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# ============================================================
# LOGIN
# ============================================================

class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in_minutes: int
    issued_at: datetime


# ============================================================
# VERIFY TOKEN
# ============================================================

class TokenVerificationResponse(BaseModel):
    valid: bool
    user_id: Optional[str]
    expires_at: Optional[datetime]


# ============================================================
# PASSWORD RESET
# ============================================================

class ResetPasswordRequest(BaseModel):
    email: str


class ResetPasswordConfirmRequest(BaseModel):
    token: str
    new_password: str


# ============================================================
# SAFE MODE
# ============================================================

class SafeModeToggleRequest(BaseModel):
    activate: bool


class SafeModeResponse(BaseModel):
    safe_mode_active: bool
    updated_at: datetime
