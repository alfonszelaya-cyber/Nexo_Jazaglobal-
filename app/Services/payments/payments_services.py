# ============================================================
# ZYRA / NEXO
# PAYMENTS SERVICE — ENTERPRISE 3.0
# Payment Processing Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.module.payments_engine import register_payment
from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class PaymentsService:
    """
    Enterprise Payments Service

    - Processes payments
    - Registers inside Core payments engine
    - Emits system-wide events
    - Writes immutable ledger trace
    """

    # ========================================================
    # PROCESS PAYMENT
    # ========================================================

    def process_payment(self, user_id: str, amount: float) -> Dict[str, Any]:

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        payment_id = str(uuid.uuid4())

        result = {
            "payment_id": payment_id,
            "user_id": user_id,
            "amount": round(amount, 2),
            "status": "processed",
            "processed_at": datetime.utcnow()
        }

        # Register inside Core module
        register_payment(result)

        # Emit infrastructure event
        route_event(
            event_type="PAYMENT_PROCESSED",
            payload=result,
            source="PAYMENTS_SERVICE"
        )

        # Immutable ledger trace
        ledger_record(
            evento="PAYMENT_PROCESSED",
            estado="SUCCESS",
            payload=result,
            origen="PAYMENTS_SERVICE"
        )

        return result

    # ========================================================
    # GET PAYMENT STATUS
    # ========================================================

    def get_payment_status(self, payment_id: str) -> Dict[str, Any]:

        if not payment_id:
            raise ValueError("Payment ID required")

        result = {
            "payment_id": payment_id,
            "status": "confirmed",
            "checked_at": datetime.utcnow()
        }

        ledger_record(
            evento="PAYMENT_STATUS_CHECK",
            estado="INFO",
            payload=result,
            origen="PAYMENTS_SERVICE"
        )

        return result
