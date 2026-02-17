# ============================================================
# ZYRA / NEXO
# USERS SCHEMA — ENTERPRISE 3.0
# Identity & User Governance Layer
# File: app/Schemas/users/users_schema.py
# ============================================================

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class UserStatusResponse(BaseModel):
    service: str
    status: str
    timestamp: datetime


# ============================================================
# CREATE USER
# ============================================================

class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    roles: Optional[List[str]] = []


class CreateUserResponse(BaseModel):
    success: bool
    message: str
    user_id: str


# ============================================================
# GET USER
# ============================================================

class GetUserRequest(BaseModel):
    user_id: str


class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    password: str
    roles: Optional[List[str]] = []
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


# ============================================================
# UPDATE USER
# ============================================================

class UpdateUserRequest(BaseModel):
    user_id: str
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    roles: Optional[List[str]] = None
    is_active: Optional[bool] = None


# ============================================================
# DELETE USER
# ============================================================

class DeleteUserRequest(BaseModel):
    user_id: str


# ============================================================
# GENERIC USER ACTION RESPONSE
# ============================================================

class UserActionResponse(BaseModel):
    success: bool
    message: str
