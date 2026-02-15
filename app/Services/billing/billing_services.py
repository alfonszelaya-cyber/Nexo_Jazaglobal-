# ============================================================
# ZYRA / NEXO
# BILLING SERVICE — ENTERPRISE 3.0
# Financial Billing Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict


class BillingService:

    @staticmethod
    def generate_invoice(client_id: str, amount: float) -> Dict:

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        return {
            "invoice_id": str(uuid.uuid4()),
            "client_id": client_id,
            "amount": round(amount, 2),
            "status": "generated",
            "created_at": datetime.utcnow()
        }

    @staticmethod
    def mark_paid(invoice_id: str) -> Dict:

        return {
            "invoice_id": invoice_id,
            "status": "paid",
            "paid_at": datetime.utcnow()
        }
