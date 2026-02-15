# ============================================================
# ZYRA / NEXO
# FINANCE SERVICE — ENTERPRISE 3.0
# Financial Core Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class FinanceService:
    """
    Enterprise Finance Service

    - Records financial transactions
    - Emits financial events
    - Registers immutable ledger traces
    - Integrates with CORE financial modules
    """

    # ========================================================
    # RECORD TRANSACTION
    # ========================================================

    def record_transaction(
        self,
        account_id: str,
        amount: float,
        tx_type: str
    ) -> Dict[str, Any]:

        if tx_type not in ["credit", "debit"]:
            raise ValueError("Transaction type must be 'credit' or 'debit'")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        result = {
            "transaction_id": str(uuid.uuid4()),
            "account_id": account_id,
            "amount": round(amount, 2),
            "type": tx_type,
            "recorded_at": datetime.utcnow()
        }

        # Emit financial event to CORE
        route_event(
            event_type="AJUSTE",
            payload=result,
            source="FINANCE_SERVICE"
        )

        # Immutable ledger trace
        ledger_record(
            evento="FINANCE_TRANSACTION",
            estado="OK",
            payload=result,
            origen="FINANCE_SERVICE"
        )

        return result

    # ========================================================
    # GENERATE FINANCIAL REPORT
    # ========================================================

    def generate_financial_report(self, entity_id: str) -> Dict[str, Any]:

        result = {
            "report_id": str(uuid.uuid4()),
            "entity_id": entity_id,
            "status": "generated",
            "generated_at": datetime.utcnow()
        }

        # Emit reporting event
        route_event(
            event_type="REPORTE_FINANCIERO",
            payload=result,
            source="FINANCE_SERVICE"
        )

        # Ledger trace
        ledger_record(
            evento="FINANCIAL_REPORT_GENERATED",
            estado="OK",
            payload=result,
            origen="FINANCE_SERVICE"
        )

        return result
