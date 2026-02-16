# ============================================================
# ZYRA / NEXO
# FINANCE SCHEMA — ENTERPRISE 3.0
# Financial Operations & Ledger Layer
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class FinanceStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# LEDGER ENTRY
# ============================================================

class LedgerEntryRequest(BaseModel):
    event: str = Field(..., description="Financial event name")
    amount: float = Field(..., ge=0)
    currency: str = Field(..., min_length=3, max_length=3)
    description: Optional[str] = None
    reference_id: Optional[str] = None


class LedgerEntryResponse(BaseModel):
    entry_id: str
    event: str
    amount: float
    currency: str
    status: str
    created_at: datetime


# ============================================================
# BALANCE
# ============================================================

class BalanceRequest(BaseModel):
    account_id: str


class BalanceResponse(BaseModel):
    account_id: str
    balance: float
    currency: str
    checked_at: datetime


# ============================================================
# CLOSE PERIOD
# ============================================================

class ClosePeriodRequest(BaseModel):
    period: str = Field(..., description="Period identifier (e.g. 2026-01)")
    reason: Optional[str] = None


class ClosePeriodResponse(BaseModel):
    period: str
    status: str
    closed_at: datetime
