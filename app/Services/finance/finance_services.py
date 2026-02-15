# ============================================================
# ZYRA / NEXO
# FINANCE SERVICE — ENTERPRISE 3.0
# Financial Core Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict


class FinanceService:

    @staticmethod
    def record_transaction(account_id: str, amount: float, type: str) -> Dict:

        if type not in ["credit", "debit"]:
            raise ValueError("Transaction type must be 'credit' or 'debit'")

        return {
            "transaction_id": str(uuid.uuid4()),
            "account_id": account_id,
            "amount": round(amount, 2),
            "type": type,
            "recorded_at": datetime.utcnow()
        }

    @staticmethod
    def generate_financial_report(entity_id: str) -> Dict:

        return {
            "report_id": str(uuid.uuid4()),
            "entity_id": entity_id,
            "status": "generated",
            "generated_at": datetime.utcnow()
        }
