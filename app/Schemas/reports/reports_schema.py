# ============================================================
# ZYRA / NEXO
# REPORTS SCHEMA — ENTERPRISE 3.0
# Financial & Operational Reporting Layer
# ============================================================

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ============================================================
# GENERATE REPORT
# ============================================================

class GenerateReportRequest(BaseModel):
    report_type: str  # FINANCIAL | SALES | TAX | INVENTORY | OPERATIONS
    start_date: datetime
    end_date: datetime
    generated_by: str


class ReportResponse(BaseModel):
    report_id: str
    report_type: str
    status: str  # GENERATED | PROCESSING | FAILED
    generated_at: datetime


# ============================================================
# REPORT DOWNLOAD REQUEST
# ============================================================

class DownloadReportRequest(BaseModel):
    report_id: str
