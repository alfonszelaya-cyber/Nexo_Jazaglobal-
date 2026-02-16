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
# DOCUMENT VALIDATION
# ============================================================

class DocumentValidationRequest(BaseModel):
    document_type: str = Field(..., description="Type of document to validate")


class DocumentValidationResponse(BaseModel):
    validation_id: str
    document_type: str
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
