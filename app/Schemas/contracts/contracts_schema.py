# ============================================================
# ZYRA / NEXO
# CONTRACTS SCHEMA — ENTERPRISE 3.0
# Contracts & Agreements Contracts Layer
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

class ContractCreateRequest(BaseModel):
    client_id: str = Field(..., description="Client identifier")
    contract_type: str = Field(..., description="Type of contract")
    amount: float = Field(..., ge=0)
    currency: str = Field(default="USD")
    start_date: datetime
    end_date: Optional[datetime] = None


class ContractCreateResponse(BaseModel):
    contract_id: str
    client_id: str
    contract_type: str
    amount: float
    currency: str
    status: str
    created_at: datetime


# ============================================================
# CONTRACT DETAIL
# ============================================================

class ContractDetailResponse(BaseModel):
    contract_id: str
    client_id: str
    contract_type: str
    amount: float
    currency: str
    status: str
    start_date: datetime
    end_date: Optional[datetime]
    created_at: datetime


# ============================================================
# UPDATE CONTRACT
# ============================================================

class ContractUpdateRequest(BaseModel):
    status: Optional[str] = None
    end_date: Optional[datetime] = None


class ContractUpdateResponse(BaseModel):
    contract_id: str
    status: str
    updated_at: datetime
