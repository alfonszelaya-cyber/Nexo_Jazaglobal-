# ============================================================
# ZYRA / NEXO
# BILLING SERVICES — ENTERPRISE 3.0
# Financial Billing Logic Layer
# File: app/Services/billing/billing_services.py
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


# ============================================================
# BILLING SERVICES CLASS
# ============================================================

class BillingServices:
    """
    Enterprise Billing Services

    - Registers ledger entries
    - Emits financial events to CORE
    - Production aligned
    """

    # ========================================================
    # CREATE INVOICE
    # ========================================================

    def create_invoice(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        amount = payload.get("amount")

        if amount is None or amount <= 0:
            raise ValueError("Amount must be greater than zero")

        invoice = {
            "invoice_id": str(uuid.uuid4()),
            "client_id": payload.get("client_id"),
            "amount": round(amount, 2),
            "currency": payload.get("currency", "USD"),
            "status": "generated",
            "created_at": datetime.utcnow()
        }

        route_event(
            event_type="INVOICE_CREATED",
            payload=invoice,
            source="BILLING_SERVICE"
        )

        ledger_record(
            evento="INVOICE_CREATED",
            estado="OK",
            payload=invoice,
            origen="BILLING_SERVICE"
        )

        return invoice

    # ========================================================
    # GET INVOICE STATUS
    # ========================================================

    def get_invoice_status(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        invoice_id = payload.get("invoice_id")

        if not invoice_id:
            raise ValueError("invoice_id is required")

        return {
            "invoice_id": invoice_id,
            "status": "generated",
            "checked_at": datetime.utcnow()
        }

    # ========================================================
    # PROCESS PAYMENT
    # ========================================================

    def process_payment(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        amount = payload.get("amount")

        if amount is None or amount <= 0:
            raise ValueError("Invalid payment amount")

        payment = {
            "payment_id": str(uuid.uuid4()),
            "invoice_id": payload.get("invoice_id"),
            "amount": round(amount, 2),
            "status": "confirmed",
            "processed_at": datetime.utcnow()
        }

        route_event(
            event_type="PAYMENT_PROCESSED",
            payload=payment,
            source="BILLING_SERVICE"
        )

        ledger_record(
            evento="PAYMENT_PROCESSED",
            estado="OK",
            payload=payment,
            origen="BILLING_SERVICE"
        )

        return payment
