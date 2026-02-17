# ============================================================
# ZYRA / NEXO
# SECURITY SCHEMA — ENTERPRISE 3.0
# Authentication & Authorization Layer
# File: app/Schemas/security/security_schema.py
# ============================================================

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class SecurityStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# TOKEN GENERATION
# ============================================================

class GenerateTokenRequest(BaseModel):
    username: str
    password: str


class GenerateTokenResponse(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"
    expires_in_minutes: int
    issued_at: datetime


# ============================================================
# TOKEN VALIDATION
# ============================================================

class ValidateTokenRequest(BaseModel):
    token: str


class ValidateTokenResponse(BaseModel):
    valid: bool
    user_id: Optional[str] = None
    roles: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
    checked_at: datetime


# ============================================================
# REFRESH TOKEN
# ============================================================

class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenResponse(BaseModel):
    access_token: str
    expires_in_minutes: int
    issued_at: datetime


# ============================================================
# API KEY GENERATION
# ============================================================

class GenerateApiKeyResponse(BaseModel):
    api_key: str
    created_at: datetime
    expires_at: Optional[datetime] = None


# ============================================================
# HASH OPERATIONS
# ============================================================

class HashRequest(BaseModel):
    value: str


class HashResponse(BaseModel):
    original: str
    hashed: str
    algorithm: str
    created_at: datetime


# ============================================================
# ACCESS VALIDATION
# ============================================================

class ValidateAccessRequest(BaseModel):
    api_key: str
    resource: str


class ValidateAccessResponse(BaseModel):
    valid: bool
    user_id: Optional[str] = None
    resource: Optional[str] = None
    checked_at: datetime
