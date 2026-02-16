# ============================================================
# ZYRA / NEXO
# BILLING SCHEMA — ENTERPRISE 3.0
# Billing Contracts Layer
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# BILLING STATUS
# ============================================================

class BillingStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# CREATE INVOICE
# ============================================================

class InvoiceCreateRequest(BaseModel):
    client_id: str
    amount: float = Field(..., gt=0)


class InvoiceStatusRequest(BaseModel):
    invoice_id: str


class PaymentProcessRequest(BaseModel):
    invoice_id: str


# ============================================================
# INVOICE RESPONSE
# ============================================================

class InvoiceResponse(BaseModel):
    invoice_id: str
    client_id: str
    amount: float
    currency: str
    status: str
    created_at: datetime


# ============================================================
# PAYMENT RESPONSE
# ============================================================

class PaymentResponse(BaseModel):
    invoice_id: str
    status: str
    paid_at: datetime
