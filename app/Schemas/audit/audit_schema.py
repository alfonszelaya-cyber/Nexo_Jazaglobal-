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
# REGISTER REQUEST  (AGREGADO PARA ALINEAR ROUTER)
# ============================================================

class AuditRegisterRequest(BaseModel):
    event_type: str = Field(..., description="Type of audited event")
    source: str = Field(..., description="Origin of the event")
    payload: Optional[Dict[str, Any]] = None


# ============================================================
# REGISTER RESPONSE  (AGREGADO PARA ALINEAR ROUTER)
# ============================================================

class AuditRegisterResponse(BaseModel):
    audit_id: str
    event_type: str
    status: str
    recorded_at: datetime


# ============================================================
# TRACE REQUEST  (AGREGADO)
# ============================================================

class AuditTraceRequest(BaseModel):
    event_type: Optional[str] = None
    source: Optional[str] = None


# ============================================================
# TRACE RESPONSE  (AGREGADO)
# ============================================================

class AuditTraceResponse(BaseModel):
    results: List[Dict[str, Any]]
    generated_at: datetime


# ============================================================
# LIST RESPONSE  (AGREGADO)
# ============================================================

class AuditListResponse(BaseModel):
    total_events: int
    events: List[Dict[str, Any]]
    timestamp: datetime


# ============================================================
# ORIGINAL CLASSES (NO TOCADO)
# ============================================================

class AuditEventRequest(BaseModel):
    event_type: str
    source: str
    payload: Optional[Dict[str, Any]] = None


class AuditEventResponse(BaseModel):
    audit_id: str
    event_type: str
    status: str
    recorded_at: datetime


class AuditReportResponse(BaseModel):
    report_id: str
    total_events: int
    errors_detected: int
    warnings_detected: int
    generated_at: datetime


class AuditLogEntry(BaseModel):
    event_type: str
    source: str
    status: str
    timestamp: datetime
    details: Optional[Dict[str, Any]] = None
