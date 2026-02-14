# ============================================================
# ZYRA / NEXO
# SYSTEM ROUTER — ENTERPRISE 3.0
# Core System Control & Monitoring
# ============================================================

from fastapi import APIRouter
from typing import Dict, Any
from datetime import datetime
import os
import platform

router = APIRouter(
    prefix="/system",
    tags=["System"]
)

# ============================================================
# STATUS
# ============================================================

@router.get("/status")
def system_status() -> Dict[str, Any]:
    return {
        "system": "ZYRA_NEXO_CORE",
        "status": "running",
        "version": "3.0.0",
        "timestamp": datetime.utcnow()
    }


# ============================================================
# SYSTEM INFO
# ============================================================

@router.get("/info")
def system_info() -> Dict[str, Any]:
    return {
        "environment": os.getenv("ENVIRONMENT", "production"),
        "platform": platform.system(),
        "platform_version": platform.version(),
        "timestamp": datetime.utcnow()
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@router.get("/health")
def system_health() -> Dict[str, Any]:
    return {
        "health": "OK",
        "checked_at": datetime.utcnow()
    }
