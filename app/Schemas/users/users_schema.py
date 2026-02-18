# ============================================================
# ZYRA / NEXO
# USERS SCHEMA — STABLE VERSION
# ============================================================

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class UserStatusResponse(BaseModel):
    module: str
    status: str
    version: str
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
    user_id: str
    username: str
    email: EmailStr
    roles: List[str]
    status: str
    created_at: datetime


# ============================================================
# GET USER
# ============================================================

class GetUserRequest(BaseModel):
    user_id: str


class UserResponse(BaseModel):
    user_id: str
    username: str
    email: EmailStr
    roles: List[str]
    status: str
    created_at: datetime


# ============================================================
# UPDATE USER
# ============================================================

class UpdateUserRequest(BaseModel):
    user_id: str
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    new_status: Optional[str] = None


# ============================================================
# DELETE USER
# ============================================================

class DeleteUserRequest(BaseModel):
    user_id: str


# ============================================================
# GENERIC USER ACTION RESPONSE
# ============================================================

class UserActionResponse(BaseModel):
    user_id: str
    action: str
    status: str
    executed_at: datetime
