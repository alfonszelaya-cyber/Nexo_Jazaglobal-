# ============================================================
# ZYRA / NEXO
# CONTRACTS ROUTER — ENTERPRISE 3.0
# Legal Agreements & Contract Lifecycle
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.contracts.contracts_schema import (
    ContractsStatusResponse,
    CreateContractRequest,
    CreateContractResponse,
    ActivateContractRequest,
    ActivateContractResponse,
    TerminateContractRequest,
    TerminateContractResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.contracts.contracts_services import ContractsService


router = APIRouter(
    prefix="/contracts",
    tags=["Contracts"]
)

contracts_service = ContractsService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=ContractsStatusResponse)
def contracts_status():
    return ContractsStatusResponse(
        module="ZYRA_CONTRACTS_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# CREATE CONTRACT
# ============================================================

@router.post("/create", response_model=CreateContractResponse)
def create_contract(payload: CreateContractRequest):
    try:
        return contracts_service.create_contract(payload)
    except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))


# ============================================================
# ACTIVATE CONTRACT
# ============================================================

@router.post("/activate", response_model=ActivateContractResponse)
def activate_contract(payload: ActivateContractRequest):
    return contracts_service.activate_contract(payload)


# ============================================================
# TERMINATE CONTRACT
# ============================================================

@router.post("/terminate", response_model=TerminateContractResponse)
def terminate_contract(payload: TerminateContractRequest):
    return contracts_service.terminate_contract(payload)
