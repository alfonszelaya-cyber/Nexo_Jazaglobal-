# ============================================================
# ZYRA / NEXO
# BILLING ROUTER — ENTERPRISE 3.0
# Billing & Subscription Management
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMA
# ============================

from app.Schemas.billing_schema import (
    BillingStatusResponse,
    InvoiceCreateRequest,
    InvoiceStatusRequest,
    PaymentProcessRequest,
    InvoiceResponse,
    PaymentResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.billing_services import BillingService


router = APIRouter(
    prefix="/billing",
    tags=["Billing"]
)

billing_service = BillingService()


# ============================================================
# BILLING STATUS
# ============================================================

@router.get("/status", response_model=BillingStatusResponse)
def billing_status():
    return BillingStatusResponse(
        module="ZYRA_BILLING_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# CREATE INVOICE
# ============================================================

@router.post("/create-invoice", response_model=InvoiceResponse)
def create_invoice(payload: InvoiceCreateRequest):
    try:
        return billing_service.create_invoice(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# GET INVOICE STATUS
# ============================================================

@router.post("/invoice-status")
def invoice_status(payload: InvoiceStatusRequest):
    return billing_service.get_invoice_status(payload)


# ============================================================
# PROCESS PAYMENT
# ============================================================

@router.post("/process-payment", response_model=PaymentResponse)
def process_payment(payload: PaymentProcessRequest):
    return billing_service.process_payment(payload)
