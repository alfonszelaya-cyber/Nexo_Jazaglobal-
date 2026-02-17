# ============================================================
# ZYRA / NEXO
# ROLES SCHEMA — ENTERPRISE 3.0
# Role & Permission Governance Layer
# File: app/Schemas/roles/roles_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class RolesStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# CREATE ROLE
# ============================================================

class CreateRoleRequest(BaseModel):
    role_name: str = Field(..., min_length=3)
    permissions: List[str]


class CreateRoleResponse(BaseModel):
    role_id: str
    role_name: str
    permissions: List[str]
    status: str  # CREATED | ACTIVE | DISABLED
    created_at: datetime


# ============================================================
# ASSIGN ROLE
# ============================================================

class AssignRoleRequest(BaseModel):
    user_id: str
    role_id: str


class AssignRoleResponse(BaseModel):
    user_id: str
    role_id: str
    assigned_at: datetime


# ============================================================
# LIST ROLES
# ============================================================

class ListRolesResponse(BaseModel):
    roles: List[CreateRoleResponse]
