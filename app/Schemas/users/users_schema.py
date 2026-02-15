# ============================================================
# ZYRA / NEXO
# USERS SCHEMA — ENTERPRISE 3.0
# Identity & User Governance Layer
# ============================================================

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


# ============================================================
# CREATE USER
# ============================================================

class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    roles: Optional[List[str]] = []


class UserResponse(BaseModel):
    user_id: str
    username: str
    email: EmailStr
    roles: List[str]
    status: str  # ACTIVE | SUSPENDED | LOCKED
    created_at: datetime


# ============================================================
# UPDATE USER STATUS
# ============================================================

class UpdateUserStatusRequest(BaseModel):
    user_id: str
    new_status: str


# ============================================================
# USER PROFILE
# ============================================================

class UserProfileResponse(BaseModel):
    user_id: str
    username: str
    email: EmailStr
    roles: List[str]
    last_login: Optional[datetime]
    status: str
