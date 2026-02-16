# ============================================================
# ZYRA / NEXO
# FINANCE ROUTER — ENTERPRISE 3.0
# Financial Operations & Ledger Layer
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.finance.finance_schema import (
    FinanceStatusResponse,
    LedgerEntryRequest,
    LedgerEntryResponse,
    BalanceRequest,
    BalanceResponse,
    ClosePeriodRequest,
    ClosePeriodResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.finance.finance_services import FinanceServices


router = APIRouter(
    prefix="/finance",
    tags=["Finance"]
)

finance_service = FinanceService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=FinanceStatusResponse)
def finance_status():
    return FinanceStatusResponse(
        module="ZYRA_FINANCE_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# CREATE LEDGER ENTRY
# ============================================================

@router.post("/ledger-entry", response_model=LedgerEntryResponse)
def create_ledger_entry(payload: LedgerEntryRequest):
    try:
        return finance_service.create_ledger_entry(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# GET BALANCE
# ============================================================

@router.post("/balance", response_model=BalanceResponse)
def get_balance(payload: BalanceRequest):
    return finance_service.get_balance(payload)


# ============================================================
# CLOSE PERIOD
# ============================================================

@router.post("/close-period", response_model=ClosePeriodResponse)
def close_period(payload: ClosePeriodRequest):
    return finance_service.close_period(payload)
