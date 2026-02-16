# ============================================================
# ZYRA / NEXO
# BILLING SERVICES — ENTERPRISE 3.0
# Financial Billing Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class BillingServices:
    """
    Enterprise Billing Services

    - Registers ledger entries
    - Emits financial events to CORE
    - Ready to connect to Finance modules or Templates
    """

    # ========================================================
    # GENERATE INVOICE
    # ========================================================

    def generate_invoice(self, client_id: str, amount: float) -> Dict[str, Any]:

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        invoice = {
            "invoice_id": str(uuid.uuid4()),
            "client_id": client_id,
            "amount": round(amount, 2),
            "currency": "USD",
            "status": "generated",
            "created_at": datetime.utcnow()
        }

        route_event(
            event_type="FACTURA_EMITIDA",
            payload=invoice,
            source="BILLING_SERVICE"
        )

        ledger_record(
            evento="INVOICE_GENERATED",
            estado="OK",
            payload=invoice,
            origen="BILLING_SERVICE"
        )

        return invoice

    # ========================================================
    # MARK INVOICE AS PAID
    # ========================================================

    def mark_paid(self, invoice_id: str) -> Dict[str, Any]:

        payment_record = {
            "invoice_id": invoice_id,
            "status": "paid",
            "paid_at": datetime.utcnow()
        }

        route_event(
            event_type="PAGO",
            payload=payment_record,
            source="BILLING_SERVICE"
        )

        ledger_record(
            evento="INVOICE_PAID",
            estado="OK",
            payload={"invoice_id": invoice_id},
            origen="BILLING_SERVICE"
        )

        return payment_record
