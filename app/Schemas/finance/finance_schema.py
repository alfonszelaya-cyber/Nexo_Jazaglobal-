# ============================================================
# ZYRA / NEXO
# FINANCE SCHEMA — ENTERPRISE 3.0
# Financial Operations & Ledger Layer
# File: app/Schemas/finance/finance_schema.py
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
# CREATE LEDGER ENTRY
# ============================================================

class CreateLedgerEntryRequest(BaseModel):
    event: str = Field(..., description="Financial event name")
    amount: float = Field(..., ge=0, description="Transaction amount")
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
# FINANCIAL REPORT REQUEST
# ============================================================

class FinancialReportRequest(BaseModel):
    period: str = Field(..., description="DAILY | MONTHLY | YEARLY")
    year: int = Field(..., ge=2000)
    month: Optional[int] = Field(None, ge=1, le=12)


class FinancialReportResponse(BaseModel):
    report_id: str
    total_income: float
    total_expenses: float
    net_result: float
    generated_at: datetime
