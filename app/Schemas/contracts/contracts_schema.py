# ============================================================
# ZYRA / NEXO
# CONTRACTS SCHEMA — ENTERPRISE 3.0
# File: app/Schemas/contracts/contracts_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class ContractsStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# CREATE CONTRACT
# ============================================================

class CreateContractRequest(BaseModel):
    client_id: str = Field(..., description="Client identifier")
    contract_type: str = Field(..., description="Type of contract")
    amount: float = Field(..., ge=0)
    currency: str = Field(default="USD")
    start_date: datetime
    end_date: Optional[datetime] = None


class CreateContractResponse(BaseModel):
    contract_id: str
    client_id: str
    contract_type: str
    amount: float
    currency: str
    status: str
    created_at: datetime


# ============================================================
# ACTIVATE CONTRACT
# ============================================================

class ActivateContractRequest(BaseModel):
    contract_id: str


class ActivateContractResponse(BaseModel):
    contract_id: str
    status: str
    activated_at: datetime


# ============================================================
# TERMINATE CONTRACT
# ============================================================

class TerminateContractRequest(BaseModel):
    contract_id: str


class TerminateContractResponse(BaseModel):
    contract_id: str
    status: str
    terminated_at: datetime
