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

class IntegrationStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# REGISTER INTEGRATION
# ============================================================

class IntegrationRegisterRequest(BaseModel):
    provider_name: str = Field(..., description="Integration provider name")
    api_key: str = Field(..., description="Provider API Key")
    environment: str = Field(..., description="SANDBOX | PRODUCTION")


class IntegrationRegisterResponse(BaseModel):
    integration_id: str
    provider_name: str
    status: str
    created_at: datetime


# ============================================================
# TEST INTEGRATION
# ============================================================

class IntegrationTestRequest(BaseModel):
    integration_id: str


class IntegrationTestResponse(BaseModel):
    integration_id: str
    connection_status: str
    tested_at: datetime


# ============================================================
# SYNC INTEGRATION
# ============================================================

class IntegrationSyncRequest(BaseModel):
    integration_id: str
    force: Optional[bool] = False


class IntegrationSyncResponse(BaseModel):
    integration_id: str
    sync_status: str
    synced_at: datetime
