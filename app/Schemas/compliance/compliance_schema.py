# ============================================================
# ZYRA / NEXO
# COMPLIANCE SCHEMA — ENTERPRISE 3.0
# Regulatory & Validation Contracts
# File: app/Schemas/compliance/compliance_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class ComplianceStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# ENTITY VALIDATION
# ============================================================

class EntityValidationRequest(BaseModel):
    entity_id: str = Field(..., description="Entity identifier to validate")
    entity_type: Optional[str] = Field(
        default=None,
        description="Optional entity classification"
    )


class EntityValidationResponse(BaseModel):
    validation_id: str
    entity_id: str
    compliant: bool
    validated_at: datetime


# ============================================================
# RISK CHECK
# ============================================================

class RiskCheckRequest(BaseModel):
    entity_id: str = Field(..., description="Entity identifier for risk analysis")


class RiskCheckResponse(BaseModel):
    risk_id: str
    entity_id: str
    risk_level: str
    checked_at: datetime
