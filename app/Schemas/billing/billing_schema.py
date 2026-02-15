# ============================================================
# ZYRA / NEXO
# BILLING SCHEMA — ENTERPRISE 3.0
# Subscription & Billing Contracts
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# CREATE SUBSCRIPTION
# ============================================================

class CreateSubscriptionRequest(BaseModel):
    user_id: str
    plan_name: str
    price_usd: float = Field(..., ge=0)
    billing_cycle: str  # monthly | yearly


class SubscriptionResponse(BaseModel):
    subscription_id: str
    user_id: str
    plan_name: str
    status: str
    started_at: datetime
    next_billing_date: Optional[datetime]


# ============================================================
# INVOICE
# ============================================================

class InvoiceResponse(BaseModel):
    invoice_id: str
    subscription_id: str
    amount: float
    currency: str
    status: str
    issued_at: datetime


# ============================================================
# PAYMENT CONFIRMATION
# ============================================================

class PaymentConfirmationResponse(BaseModel):
    payment_id: str
    invoice_id: str
    status: str
    confirmed_at: datetime
