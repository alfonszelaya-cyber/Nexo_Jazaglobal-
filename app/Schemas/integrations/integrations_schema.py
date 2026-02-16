# ============================================================
# ZYRA / NEXO
# INTEGRATIONS SCHEMA — ENTERPRISE 3.0
# External Systems Integration Layer
# File: app/Schemas/integrations/integrations_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class IntegrationsStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# REGISTER INTEGRATION
# ============================================================

class RegisterIntegrationRequest(BaseModel):
    provider_name: str = Field(..., description="Integration provider name")
    api_key: str = Field(..., description="Provider API Key")
    environment: str = Field(..., description="SANDBOX | PRODUCTION")


class IntegrationResponse(BaseModel):
    integration_id: str
    provider_name: str
    status: str  # ACTIVE | INACTIVE
    created_at: datetime


# ============================================================
# TEST CONNECTION
# ============================================================

class TestConnectionRequest(BaseModel):
    integration_id: str


class TestConnectionResponse(BaseModel):
    integration_id: str
    connection_status: str
    tested_at: datetime


# ============================================================
# WEBHOOK EVENT
# ============================================================

class WebhookEventRequest(BaseModel):
    provider_name: str
    event_type: str
    payload: Dict[str, Any]
    received_at: datetime


class WebhookEventResponse(BaseModel):
    event_id: str
    provider_name: str
    event_type: str
    status: str
    processed_at: datetime
