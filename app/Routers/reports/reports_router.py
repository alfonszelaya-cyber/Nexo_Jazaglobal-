# ============================================================
# ZYRA / NEXO
# REPORTS ROUTER — ENTERPRISE 3.0
# Reporting & Business Intelligence Layer
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.reports.reports_schema import (
    ReportsStatusResponse,
    GenerateReportRequest,
    GenerateReportResponse,
    GetReportRequest,
    GetReportResponse,
    ListReportsResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.reports.reports_services import ReportsService


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

reports_service = ReportsService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=ReportsStatusResponse)
def reports_status():
    return ReportsStatusResponse(
        module="ZYRA_REPORTS_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# GENERATE REPORT
# ============================================================

@router.post("/generate", response_model=GenerateReportResponse)
def generate_report(payload: GenerateReportRequest):
    try:
        return reports_service.generate_report(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# GET REPORT
# ============================================================

@router.post("/get", response_model=GetReportResponse)
def get_report(payload: GetReportRequest):
    return reports_service.get_report(payload)


# ============================================================
# LIST REPORTS
# ============================================================

@router.get("/list", response_model=ListReportsResponse)
def list_reports():
    return reports_service.list_reports()
