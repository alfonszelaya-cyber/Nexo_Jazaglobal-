# ============================================================
# ZYRA / NEXO
# AUDIT SCHEMA — ENTERPRISE 3.0
# Audit & Compliance Contracts Layer
# ============================================================

from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime


# ============================================================
# AUDIT STATUS RESPONSE
# ============================================================

class AuditStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# AUDIT EVENT REQUEST
# ============================================================

class AuditEventRequest(BaseModel):
    event_type: str = Field(..., description="Type of audited event")
    source: str = Field(..., description="Origin of the event")
    payload: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Event data payload"
    )


# ============================================================
# AUDIT EVENT RESPONSE
# ============================================================

class AuditEventResponse(BaseModel):
    audit_id: str
    event_type: str
    status: str
    recorded_at: datetime


# ============================================================
# AUDIT REPORT RESPONSE
# ============================================================

class AuditReportResponse(BaseModel):
    report_id: str
    total_events: int
    errors_detected: int
    warnings_detected: int
    generated_at: datetime


# ============================================================
# AUDIT LOG ENTRY
# ============================================================

class AuditLogEntry(BaseModel):
    event_type: str
    source: str
    status: str
    timestamp: datetime
    details: Optional[Dict[str, Any]] = None
