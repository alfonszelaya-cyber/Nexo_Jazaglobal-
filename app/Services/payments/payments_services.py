# ============================================================
# ZYRA / NEXO
# PAYMENTS SERVICE — ENTERPRISE 3.0
# Payment Processing Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict


class PaymentsService:

    @staticmethod
    def process_payment(user_id: str, amount: float) -> Dict:

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        return {
            "payment_id": str(uuid.uuid4()),
            "user_id": user_id,
            "amount": amount,
            "status": "processed",
            "processed_at": datetime.utcnow()
        }

    @staticmethod
    def get_payment_status(payment_id: str) -> Dict:

        return {
            "payment_id": payment_id,
            "status": "confirmed",
            "checked_at": datetime.utcnow()
        }
