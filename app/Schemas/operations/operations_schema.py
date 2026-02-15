# ============================================================
# ZYRA / NEXO
# OPERATIONS SCHEMA — ENTERPRISE 3.0
# Workflow & Automation Control Layer
# ============================================================

from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


# ============================================================
# EXECUTE OPERATION
# ============================================================

class ExecuteOperationRequest(BaseModel):
    operation_type: str  # IMPORT | EXPORT | INTERNAL | AUTOMATION
    payload: Dict[str, Any]
    initiated_by: str


class OperationResponse(BaseModel):
    operation_id: str
    operation_type: str
    status: str  # CREATED | RUNNING | COMPLETED | FAILED
    started_at: datetime


# ============================================================
# UPDATE OPERATION STATUS
# ============================================================

class UpdateOperationStatusRequest(BaseModel):
    operation_id: str
    new_status: str
    updated_at: datetime
