# ============================================================
# FINANCE ROUTER — NEXO ENTERPRISE
# ============================================================

from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from application.use_cases.finance.generate_sales_finance_report_use_case import (
    GenerateSalesFinanceReportUseCase,
)

router = APIRouter(prefix="/finance", tags=["Finance"])


@router.post("/sales-report")
def generate_sales_report(payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        use_case = GenerateSalesFinanceReportUseCase()
        result = use_case.execute(payload)

        return {
            "success": True,
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
