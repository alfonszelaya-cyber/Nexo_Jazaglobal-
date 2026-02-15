# ============================================================
# ZYRA / NEXO
# PAYMENTS ROUTER — ENTERPRISE 3.0
# Payment Processing & Transaction Control
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.payments_schema import (
    PaymentsStatusResponse,
    InitiatePaymentRequest,
    InitiatePaymentResponse,
    ConfirmPaymentRequest,
    ConfirmPaymentResponse,
    PaymentStatusRequest,
    PaymentStatusResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.payments_services import PaymentsService


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

payments_service = PaymentsService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=PaymentsStatusResponse)
def payments_status():
    return PaymentsStatusResponse(
        module="ZYRA_PAYMENTS_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# INITIATE PAYMENT
# ============================================================

@router.post("/initiate", response_model=InitiatePaymentResponse)
def initiate_payment(payload: InitiatePaymentRequest):
    try:
        return payments_service.initiate_payment(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# CONFIRM PAYMENT
# ============================================================

@router.post("/confirm", response_model=ConfirmPaymentResponse)
def confirm_payment(payload: ConfirmPaymentRequest):
    return payments_service.confirm_payment(payload)


# ============================================================
# PAYMENT STATUS
# ============================================================

@router.post("/status-check", response_model=PaymentStatusResponse)
def payment_status(payload: PaymentStatusRequest):
    return payments_service.get_payment_status(payload)
