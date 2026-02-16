# ============================================================
# ZYRA / NEXO
# AI ROUTER — ENTERPRISE 3.0
# Conectado a Schemas + Services (Real Architecture)
# ============================================================

from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime

# ===============================
# IMPORT SCHEMAS
# ===============================

from app.Schemas.analytics.analytics_schema import (
    AnalyticsStatusResponse,
    MetricRequest,
    MetricResponse
)

# ===============================
# IMPORT SERVICES
# ===============================

from app.Services.analytics.analytics_services import AnalyticsServices


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

# ===============================
# DEPENDENCY INJECTION
# ===============================

def get_service():
    return AnalyticsServices()


# ============================================================
# AI STATUS
# ============================================================

@router.get("/status", response_model=AnalyticsStatusResponse)
def ai_status():
    return AnalyticsStatusResponse(
        module="ZYRA_AI_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# AI ANALYZE (REAL SERVICE CALL)
# ============================================================

@router.post("/analyze", response_model=MetricResponse)
def analyze_data(
    payload: MetricRequest,
    service: AnalyticsServices = Depends(get_service)
):
    try:
        return service.generate_kpi_summary(payload.dict())

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# ============================================================
# AI PREDICT (REAL SERVICE CALL)
# ============================================================

@router.post("/predict", response_model=MetricResponse)
def predict(
    payload: MetricRequest,
    service: AnalyticsServices = Depends(get_service)
):
    try:
        return service.forecast(payload.dict())

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
