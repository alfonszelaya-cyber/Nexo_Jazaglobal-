# ============================================================
# ZYRA / NEXO
# CONTRACTS SCHEMA — ENTERPRISE 3.0
# Legal & Business Agreement Contracts
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ============================================================
# CREATE CONTRACT
# ============================================================

class CreateContractRequest(BaseModel):
    contract_name: str
    party_a: str
    party_b: str
    effective_date: datetime
    expiration_date: Optional[datetime]
    currency: str
    total_value: float = Field(..., ge=0)


class ContractResponse(BaseModel):
    contract_id: str
    contract_name: str
    party_a: str
    party_b: str
    status: str  # DRAFT | ACTIVE | TERMINATED | EXPIRED
    created_at: datetime


# ============================================================
# CONTRACT AMENDMENT
# ============================================================

class ContractAmendmentRequest(BaseModel):
    contract_id: str
    amendment_reason: str
    updated_value: Optional[float]
    updated_expiration: Optional[datetime]


class ContractAmendmentResponse(BaseModel):
    amendment_id: str
    contract_id: str
    status: str
    amended_at: datetime


# ============================================================
# CONTRACT SUMMARY
# ============================================================

class ContractSummary(BaseModel):
    total_contracts: int
    active_contracts: int
    expired_contracts: int
    terminated_contracts: int
    generated_at: datetime
