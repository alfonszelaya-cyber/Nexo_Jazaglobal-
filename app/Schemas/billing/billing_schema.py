# ============================================================
# ZYRA / NEXO
# BILLING SCHEMA — ENTERPRISE 3.0
# Billing & Subscription Contracts
# File: app/Schemas/billing/billing_schema.py
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


class InvoiceResponse(BaseModel):
    invoice_id: str
    client_id: str
    amount: float
    currency: str
    status: str
    created_at: datetime


# ============================================================
# INVOICE STATUS
# ============================================================

class InvoiceStatusRequest(BaseModel):
    invoice_id: str


# ============================================================
# PAYMENT PROCESS
# ============================================================

class PaymentProcessRequest(BaseModel):
    invoice_id: str
    amount: float = Field(..., gt=0)


class PaymentResponse(BaseModel):
    payment_id: str
    invoice_id: str
    status: str
    processed_at: datetime
