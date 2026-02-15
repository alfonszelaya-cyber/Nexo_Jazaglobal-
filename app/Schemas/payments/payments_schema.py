# ============================================================
# ZYRA / NEXO
# PAYMENTS SCHEMA — ENTERPRISE 3.0
# Universal Payment Processing Layer
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# CREATE PAYMENT
# ============================================================

class CreatePaymentRequest(BaseModel):
    payer_id: str
    receiver_id: str
    amount: float = Field(..., gt=0)
    currency: str
    method: str  # CASH | CARD | TRANSFER | CRYPTO
    reference: Optional[str]


class PaymentResponse(BaseModel):
    payment_id: str
    payer_id: str
    receiver_id: str
    amount: float
    currency: str
    status: str  # PENDING | COMPLETED | FAILED | CANCELLED
    created_at: datetime


# ============================================================
# PAYMENT STATUS UPDATE
# ============================================================

class UpdatePaymentStatusRequest(BaseModel):
    payment_id: str
    new_status: str
    updated_at: datetime
