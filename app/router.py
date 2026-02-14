# ============================================================
# ZYRA / NEXO
# API ROUTER — ENTERPRISE 3.0
# Clean Architecture | Production Ready | Scalable
# ============================================================

from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from application.use_cases.finance.generate_sales_finance_report_use_case import (
    GenerateSalesFinanceReportUseCase,
)

router = APIRouter(prefix="/api/v1", tags=["Finance"])


# ============================================================
# HEALTH CHECK
# ============================================================

@router.get("/health")
def health_check() -> Dict[str, Any]:
    return {
        "status": "OK",
        "service": "NEXO_ZYRA_CORE",
        "version": "3.0"
    }


# ============================================================
# GENERATE SALES FINANCE REPORT
# ============================================================

@router.post("/finance/sales-report")
def generate_sales_report(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates a Sales Finance Report using official template registry.
    """

    try:
        use_case = GenerateSalesFinanceReportUseCase()
        result = use_case.execute(payload)

        return {
            "success": True,
            "message": "Sales finance report generated successfully",
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={
                "success": False,
                "error": "SALES_FINANCE_REPORT_GENERATION_FAILED",
                "message": str(e)
            }
        )
