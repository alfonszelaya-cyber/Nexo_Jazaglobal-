# ============================================================
# ZYRA / NEXO
# ROLES SCHEMA — ENTERPRISE 3.0
# Role & Permission Governance Layer
# ============================================================

from pydantic import BaseModel
from typing import List
from datetime import datetime


# ============================================================
# CREATE ROLE
# ============================================================

class CreateRoleRequest(BaseModel):
    role_name: str
    permissions: List[str]


class RoleResponse(BaseModel):
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
# ROLE STATUS UPDATE
# ============================================================

class UpdateRoleStatusRequest(BaseModel):
    role_id: str
    new_status: str
