# ============================================================
# ZYRA / NEXO
# ANALYTICS ROUTER — ENTERPRISE 3.0
# Conectado a Schemas + Services
# ============================================================

from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime

# ===============================
# IMPORT SCHEMAS
# ===============================

from app.Schemas.analytics.analytics_schema import (
    AnalyticsStatusResponse,
    KPIRequest,
    KPIResponse,
    TrendRequest,
    TrendResponse,
    ForecastRequest,
    ForecastResponse
)

# ===============================
# IMPORT SERVICES
# ===============================

from app.Services.analytics.analytics_services import AnalyticsServices


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# ===============================
# DEPENDENCY
# ===============================

def get_service():
    return AnalyticsServices()


# ============================================================
# ANALYTICS STATUS
# ============================================================

@router.get("/status", response_model=AnalyticsStatusResponse)
def analytics_status():
    return AnalyticsStatusResponse(
        module="ZYRA_ANALYTICS_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# KPI SUMMARY
# ============================================================

@router.post("/kpi-summary", response_model=KPIResponse)
def generate_kpi_summary(
    payload: KPIRequest,
    service: AnalyticsServices = Depends(get_service)
):
    try:
        return service.generate_kpi_summary(payload.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# TREND ANALYSIS
# ============================================================

@router.post("/trend-analysis", response_model=TrendResponse)
def trend_analysis(
    payload: TrendRequest,
    service: AnalyticsServices = Depends(get_service)
):
    try:
        return service.trend_analysis(payload.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# FORECAST ENGINE
# ============================================================

@router.post("/forecast", response_model=ForecastResponse)
def forecast(
    payload: ForecastRequest,
    service: AnalyticsServices = Depends(get_service)
):
    try:
        return service.forecast(payload.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
