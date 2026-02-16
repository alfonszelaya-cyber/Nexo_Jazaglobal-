# ============================================================
# ZYRA / NEXO
# SYSTEM ROUTER — ENTERPRISE 3.0
# Core System Control & Monitoring
# ============================================================

from fastapi import APIRouter
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.system.system_schema import (
    SystemStatusResponse,
    SystemInfoResponse,
    SystemHealthResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.system.system_services import SystemService


router = APIRouter(
    prefix="/system",
    tags=["System"]
)

system_service = SystemService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=SystemStatusResponse)
def system_status():
    return system_service.get_status()


# ============================================================
# SYSTEM INFO
# ============================================================

@router.get("/info", response_model=SystemInfoResponse)
def system_info():
    return system_service.get_system_info()


# ============================================================
# HEALTH CHECK
# ============================================================

@router.get("/health", response_model=SystemHealthResponse)
def system_health():
    return system_service.get_health()
