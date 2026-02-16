# ============================================================
# ZYRA / NEXO
# OPERATIONS SCHEMA — ENTERPRISE 3.0
# Workflow & Automation Control Layer
# File: app/Schemas/operations/operations_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class OperationsStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# EXECUTE OPERATION
# ============================================================

class ExecuteOperationRequest(BaseModel):
    operation_type: str = Field(..., description="IMPORT | EXPORT | INTERNAL | AUTOMATION")
    payload: Dict[str, Any]
    initiated_by: str


class ExecuteOperationResponse(BaseModel):
    operation_id: str
    operation_type: str
    status: str  # CREATED | RUNNING | COMPLETED | FAILED
    started_at: datetime


# ============================================================
# OPERATION STATUS
# ============================================================

class OperationStatusRequest(BaseModel):
    operation_id: str


class OperationStatusResponse(BaseModel):
    operation_id: str
    operation_type: str
    status: str
    started_at: datetime
    completed_at: Optional[datetime] = None


# ============================================================
# CANCEL OPERATION
# ============================================================

class CancelOperationRequest(BaseModel):
    operation_id: str
    cancelled_by: str


class CancelOperationResponse(BaseModel):
    operation_id: str
    status: str  # CANCELLED
    cancelled_at: datetime
