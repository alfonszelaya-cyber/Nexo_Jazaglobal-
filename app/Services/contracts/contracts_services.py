# ============================================================
# ZYRA / NEXO
# CONTRACTS SERVICE — ENTERPRISE 3.0
# Contract Management Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class ContractsService:
    """
    Enterprise Contracts Service

    - Creates and terminates contracts
    - Emits legal events to CORE
    - Registers immutable ledger records
    """

    # ========================================================
    # CREATE CONTRACT
    # ========================================================

    def create_contract(self, party_a: str, party_b: str, value: float) -> Dict[str, Any]:

        if value <= 0:
            raise ValueError("Contract value must be greater than zero")

        result = {
            "contract_id": str(uuid.uuid4()),
            "party_a": party_a,
            "party_b": party_b,
            "value": round(value, 2),
            "status": "active",
            "created_at": datetime.utcnow()
        }

        # Emit legal event
        route_event(
            event_type="DECISION_ZYRA",
            payload=result,
            source="CONTRACTS_SERVICE"
        )

        # Ledger trace
        ledger_record(
            evento="CONTRACT_CREATED",
            estado="OK",
            payload=result,
            origen="CONTRACTS_SERVICE"
        )

        return result

    # ========================================================
    # TERMINATE CONTRACT
    # ========================================================

    def terminate_contract(self, contract_id: str) -> Dict[str, Any]:

        result = {
            "contract_id": contract_id,
            "status": "terminated",
            "terminated_at": datetime.utcnow()
        }

        # Emit legal termination event
        route_event(
            event_type="DECISION_ZYRA",
            payload=result,
            source="CONTRACTS_SERVICE"
        )

        # Ledger trace
        ledger_record(
            evento="CONTRACT_TERMINATED",
            estado="OK",
            payload=result,
            origen="CONTRACTS_SERVICE"
        )

        return result
