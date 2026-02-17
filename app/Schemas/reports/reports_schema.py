# ============================================================
# ZYRA / NEXO
# REPORTS SCHEMA — ENTERPRISE 3.0
# Financial & Operational Reporting Layer
# File: app/Schemas/reports/reports_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class ReportsStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# GENERATE REPORT
# ============================================================

class GenerateReportRequest(BaseModel):
    report_type: str = Field(..., description="FINANCIAL | SALES | TAX | INVENTORY | OPERATIONS")
    start_date: datetime
    end_date: datetime
    generated_by: str


class GenerateReportResponse(BaseModel):
    report_id: str
    report_type: str
    status: str  # GENERATED | PROCESSING | FAILED
    generated_at: datetime


# ============================================================
# GET REPORT
# ============================================================

class GetReportRequest(BaseModel):
    report_id: str


class GetReportResponse(BaseModel):
    report_id: str
    report_type: str
    status: str
    generated_at: datetime
    download_url: str


# ============================================================
# LIST REPORTS
# ============================================================

class ListReportsResponse(BaseModel):
    reports: List[GetReportResponse]
