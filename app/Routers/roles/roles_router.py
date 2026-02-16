# ============================================================
# ZYRA / NEXO
# ROLES ROUTER — ENTERPRISE 3.0
# Role & Permission Management Layer
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.roles.roles_schema import (
    RolesStatusResponse,
    CreateRoleRequest,
    CreateRoleResponse,
    AssignRoleRequest,
    AssignRoleResponse,
    ListRolesResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.roles.roles_services import RolesService


router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

roles_service = RolesService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=RolesStatusResponse)
def roles_status():
    return RolesStatusResponse(
        module="ZYRA_ROLES_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# CREATE ROLE
# ============================================================

@router.post("/create", response_model=CreateRoleResponse)
def create_role(payload: CreateRoleRequest):
    try:
        return roles_service.create_role(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# ASSIGN ROLE
# ============================================================

@router.post("/assign", response_model=AssignRoleResponse)
def assign_role(payload: AssignRoleRequest):
    return roles_service.assign_role(payload)


# ============================================================
# LIST ROLES
# ============================================================

@router.get("/list", response_model=ListRolesResponse)
def list_roles():
    return roles_service.list_roles()
