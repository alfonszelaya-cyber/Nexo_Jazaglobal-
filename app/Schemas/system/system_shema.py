# ============================================================
# ZYRA / NEXO
# SYSTEM SCHEMA — ENTERPRISE 3.0
# Core System Governance Layer
# ============================================================

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# ============================================================
# SYSTEM STATUS
# ============================================================

class SystemStatusResponse(BaseModel):
    system_name: str
    version: str
    state: str  # BOOTING | READY | SAFE | DEGRADED | SHUTDOWN
    uptime_seconds: Optional[int]
    timestamp: datetime


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
