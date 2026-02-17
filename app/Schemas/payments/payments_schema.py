
# ============================================================
# ZYRA / NEXO
# PAYMENTS SCHEMA — ENTERPRISE 3.0
# Universal Payment Processing Layer
# File: app/Schemas/payments/payments_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class PaymentsStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# INITIATE PAYMENT
# ============================================================

class InitiatePaymentRequest(BaseModel):
    payer_id: str = Field(..., description="User initiating payment")
    receiver_id: str = Field(..., description="Payment recipient")
    amount: float = Field(..., gt=0, description="Payment amount")
    currency: str = Field(..., min_length=3, max_length=3)
    method: str = Field(..., description="CASH | CARD | TRANSFER | CRYPTO")
    reference: Optional[str] = None


class InitiatePaymentResponse(BaseModel):
    payment_id: str
    payer_id: str
    receiver_id: str
    amount: float
    currency: str
    method: str
    status: str  # PENDING
    created_at: datetime


# ============================================================
# CONFIRM PAYMENT
# ============================================================

class ConfirmPaymentRequest(BaseModel):
    payment_id: str


class ConfirmPaymentResponse(BaseModel):
    payment_id: str
    status: str  # COMPLETED | FAILED
    confirmed_at: datetime


# ============================================================
# PAYMENT STATUS CHECK
# ============================================================

class PaymentStatusRequest(BaseModel):
    payment_id: str


class PaymentStatusResponse(BaseModel):
    payment_id: str
    status: str  # PENDING | COMPLETED | FAILED | CANCELLED
    last_updated: datetime
