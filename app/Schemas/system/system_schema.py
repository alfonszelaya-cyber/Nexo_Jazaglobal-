# ============================================================
# ZYRA / NEXO
# SYSTEM SCHEMA — ENTERPRISE 3.0
# Core System Governance Layer
# File: app/Schemas/system/system_schema.py
# ============================================================

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any


# ============================================================
# SYSTEM STATUS
# ============================================================

class SystemStatusResponse(BaseModel):
    system_name: str
    version: str
    state: str  # BOOTING | READY | SAFE | DEGRADED | SHUTDOWN
    uptime_seconds: Optional[int] = None
    timestamp: datetime


# ============================================================
# SYSTEM INFO
# ============================================================

class SystemInfoResponse(BaseModel):
    system_name: str
    version: str
    environment: str  # DEVELOPMENT | STAGING | PRODUCTION
    build_number: Optional[str] = None
    started_at: datetime


# ============================================================
# SYSTEM HEALTH
# ============================================================

class SystemHealthResponse(BaseModel):
    status: str  # HEALTHY | DEGRADED | CRITICAL
    database: str  # CONNECTED | DISCONNECTED
    cache: Optional[str] = None
    dependencies: Optional[Dict[str, Any]] = None
    checked_at: datetime


# ============================================================
# BOOT SYSTEM
# ============================================================

class BootSystemResponse(BaseModel):
    status: str  # BOOT_OK | BOOT_SAFE | BOOT_HALT
    checked_at: datetime


# ============================================================
# SHUTDOWN SYSTEM
# ============================================================

class ShutdownSystemRequest(BaseModel):
    reason: str


class ShutdownSystemResponse(BaseModel):
    status: str  # SHUTDOWN_INITIATED | SHUTDOWN_COMPLETED
    executed_at: datetime
