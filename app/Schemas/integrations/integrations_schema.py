# ============================================================
# ZYRA / NEXO
# INTEGRATIONS SCHEMA — ENTERPRISE 3.0
# External Systems Integration Layer
# ============================================================

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ============================================================
# REGISTER INTEGRATION
# ============================================================

class RegisterIntegrationRequest(BaseModel):
    provider_name: str
    api_key: str
    environment: str  # SANDBOX | PRODUCTION


class IntegrationResponse(BaseModel):
    integration_id: str
    provider_name: str
    status: str  # ACTIVE | INACTIVE
    created_at: datetime


# ============================================================
# WEBHOOK EVENT
# ============================================================

class WebhookEvent(BaseModel):
    provider_name: str
    event_type: str
    payload: dict
    received_at: datetime
