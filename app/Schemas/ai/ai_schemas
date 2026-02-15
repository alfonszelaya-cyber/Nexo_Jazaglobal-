# ============================================================
# ZYRA / NEXO
# AI SCHEMA — ENTERPRISE 3.0
# Artificial Intelligence Data Contracts
# ============================================================

from pydantic import BaseModel, Field
from typing import Any, Dict, Optional
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class AIStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# ANALYZE REQUEST
# ============================================================

class AIAnalyzeRequest(BaseModel):
    payload: Dict[str, Any] = Field(
        ...,
        description="Data to be analyzed by AI engine"
    )


# ============================================================
# ANALYZE RESPONSE
# ============================================================

class AIAnalyzeResponse(BaseModel):
    analysis_id: str
    insight: str
    confidence_score: float
    generated_at: datetime


# ============================================================
# PREDICT REQUEST
# ============================================================

class AIPredictRequest(BaseModel):
    input_data: Dict[str, Any] = Field(
        ...,
        description="Input data for prediction engine"
    )


# ============================================================
# PREDICT RESPONSE
# ============================================================

class AIPredictResponse(BaseModel):
    prediction_id: str
    prediction: str
    probability: float
    generated_at: datetime
