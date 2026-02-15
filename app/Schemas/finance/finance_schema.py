# ============================================================
# ZYRA / NEXO
# FINANCE SCHEMA — ENTERPRISE 3.0
# Financial Operations & Ledger Layer
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# LEDGER ENTRY
# ============================================================

class CreateLedgerEntryRequest(BaseModel):
    event: str
    amount: float = Field(..., ge=0)
    currency: str
    description: Optional[str]
    reference_id: Optional[str]


class LedgerEntryResponse(BaseModel):
    entry_id: str
    event: str
    amount: float
    currency: str
    status: str
    created_at: datetime


# ============================================================
# FINANCIAL REPORT REQUEST
# ============================================================

class FinancialReportRequest(BaseModel):
    period: str  # DAILY | MONTHLY | YEARLY
    year: int
    month: Optional[int]


class FinancialReportResponse(BaseModel):
    report_id: str
    total_income: float
    total_expenses: float
    net_result: float
    generated_at: datetime
