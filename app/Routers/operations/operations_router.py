# ============================================================
# ZYRA / NEXO
# OPERATIONS ROUTER — ENTERPRISE 3.0
# Operational Execution & Workflow Control
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.operations.operations_schema import (
    OperationsStatusResponse,
    ExecuteOperationRequest,
    ExecuteOperationResponse,
    OperationStatusRequest,
    OperationStatusResponse,
    CancelOperationRequest,
    CancelOperationResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.operations.operations_services import OperationsService


router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)

operations_service = OperationsService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=OperationsStatusResponse)
def operations_status():
    return OperationsStatusResponse(
        module="ZYRA_OPERATIONS_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# EXECUTE OPERATION
# ============================================================

@router.post("/execute", response_model=ExecuteOperationResponse)
def execute_operation(payload: ExecuteOperationRequest):
    try:
        return operations_service.execute_operation(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# OPERATION STATUS
# ============================================================

@router.post("/status-check", response_model=OperationStatusResponse)
def operation_status(payload: OperationStatusRequest):
    return operations_service.get_operation_status(payload)


# ============================================================
# CANCEL OPERATION
# ============================================================

@router.post("/cancel", response_model=CancelOperationResponse)
def cancel_operation(payload: CancelOperationRequest):
    return operations_service.cancel_operation(payload)
