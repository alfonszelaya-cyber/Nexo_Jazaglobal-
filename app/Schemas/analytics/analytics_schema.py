# ============================================================
# ZYRA / NEXO
# ANALYTICS SCHEMA — ENTERPRISE 3.0
# Data Analytics Contracts Layer
# ============================================================

from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime


# ============================================================
# ANALYTICS STATUS RESPONSE
# ============================================================

class AnalyticsStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# METRIC REQUEST
# ============================================================

class MetricRequest(BaseModel):
    metric_name: str = Field(..., description="Name of the metric")
    filters: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional filters for metric calculation"
    )


# ============================================================
# METRIC RESPONSE
# ============================================================

class MetricResponse(BaseModel):
    metric_id: str
    metric_name: str
    value: float
    generated_at: datetime


# ============================================================
# DASHBOARD REQUEST
# ============================================================

class DashboardRequest(BaseModel):
    dashboard_name: str
    metrics: List[str]
    filters: Optional[Dict[str, Any]] = None


# ============================================================
# DASHBOARD RESPONSE
# ============================================================

class DashboardResponse(BaseModel):
    dashboard_id: str
    dashboard_name: str
    metrics: Dict[str, float]
    generated_at: datetime


# ============================================================
# KPI REQUEST (COMPATIBILIDAD CON ROUTER)
# ============================================================

class KPIRequest(BaseModel):
    kpi_name: str = Field(..., description="Name of the KPI")
    filters: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional filters for KPI calculation"
    )


# ============================================================
# KPI RESPONSE (COMPATIBILIDAD CON ROUTER)
# ============================================================

class KPIResponse(BaseModel):
    kpi_id: str
    kpi_name: str
    value: float
    calculated_at: datetime


# ============================================================
# FORECAST REQUEST (COMPATIBILIDAD CON ROUTER)
# ============================================================

class ForecastRequest(BaseModel):
    forecast_type: str = Field(..., description="Type of forecast (sales, revenue, growth, etc)")
    period: str = Field(..., description="Forecast period (monthly, quarterly, yearly)")
    filters: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional filters for forecast calculation"
    )


# ============================================================
# FORECAST RESPONSE (COMPATIBILIDAD CON ROUTER)
# ============================================================

class ForecastResponse(BaseModel):
    forecast_id: str
    forecast_type: str
    period: str
    predicted_value: float
    generated_at: datetime
