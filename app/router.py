# ============================================================
# ZYRA / NEXO
# API ROUTER — ENTERPRISE 3.0
# Clean Architecture | Production Ready | Scalable
# ============================================================

from fastapi import APIRouter, HTTPException
from application.use_cases.finance.generate_sales_finance_report_use_case import (
    GenerateSalesFinanceReportUseCase,
)

router = APIRouter()


# ============================================================
# HEALTH CHECK
# ============================================================

@router.get("/health")
def health_check():
    return {
        "status": "OK",
        "service": "NEXO_ZYRA_CORE",
        "version": "3.0"
    }


# ============================================================
# SALES FINANCE REPORT
# ============================================================

@router.post("/finance/sales-report")
def generate_sales_report(payload: dict):

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
            detail=f"Error generating sales finance report: {str(e)}"
        )
