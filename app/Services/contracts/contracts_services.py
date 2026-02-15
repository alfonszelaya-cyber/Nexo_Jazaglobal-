# ============================================================
# ZYRA / NEXO
# CONTRACTS SERVICE — ENTERPRISE 3.0
# Contract Management Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict


class ContractsService:

    @staticmethod
    def create_contract(party_a: str, party_b: str, value: float) -> Dict:

        if value <= 0:
            raise ValueError("Contract value must be greater than zero")

        return {
            "contract_id": str(uuid.uuid4()),
            "party_a": party_a,
            "party_b": party_b,
            "value": round(value, 2),
            "status": "active",
            "created_at": datetime.utcnow()
        }

    @staticmethod
    def terminate_contract(contract_id: str) -> Dict:

        return {
            "contract_id": contract_id,
            "status": "terminated",
            "terminated_at": datetime.utcnow()
        }
