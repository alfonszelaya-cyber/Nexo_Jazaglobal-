# ============================================================
# ZYRA / NEXO
# BILLING ROUTER — ENTERPRISE 3.0
# Billing & Subscription Management
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.billing.billing_schema import (
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

from app.Services.billing.billing_services import BillingServices


router = APIRouter(
    prefix="/billing",
    tags=["Billing"]
)

billing_service = BillingServices()


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
        return billing_service.generate_invoice(
            client_id=payload.client_id,
            amount=payload.amount
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# INVOICE STATUS
# ============================================================

@router.post("/invoice-status")
def invoice_status(payload: InvoiceStatusRequest):
    return {
        "invoice_id": payload.invoice_id,
        "status": "generated"
    }


# ============================================================
# PROCESS PAYMENT
# ============================================================

@router.post("/process-payment", response_model=PaymentResponse)
def process_payment(payload: PaymentProcessRequest):
    return billing_service.mark_paid(payload.invoice_id)
