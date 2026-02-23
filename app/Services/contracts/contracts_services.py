# ============================================================
# ZYRA / NEXO
# CONTRACTS SERVICE — ENTERPRISE 3.1 (STABLE FIX)
# Contract Management Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class ContractsService:

    # ========================================================
    # CREATE CONTRACT
    # ========================================================

    def create_contract(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        client_id = payload.get("client_id")
        contract_type = payload.get("contract_type")
        amount = payload.get("amount")
        currency = payload.get("currency")
        start_date = payload.get("start_date")
        end_date = payload.get("end_date")

        if not client_id or not contract_type:
            raise ValueError("client_id and contract_type required")

        if amount is None or amount <= 0:
            raise ValueError("Contract amount must be greater than zero")

        result = {
            "id": uuid.uuid4().hex,
            "contract_id": uuid.uuid4().hex,
            "client_id": client_id,
            "contract_type": contract_type,
            "amount": round(float(amount), 2),
            "currency": currency,
            "start_date": start_date,
            "end_date": end_date,
            "status": "active",
            "created_at": datetime.utcnow().isoformat()
        }

        route_event(
            event_type="DECISION_ZYRA",
            payload=result,
            source="CONTRACTS_SERVICE"
        )

        ledger_record(
            evento="CONTRACT_CREATED",
            estado="OK",
            payload={"contract_id": result["contract_id"]},
            origen="CONTRACTS_SERVICE"
        )

        return result

    # ========================================================
    # ACTIVATE CONTRACT
    # ========================================================

    def activate_contract(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        contract_id = payload.get("contract_id")

        if not contract_id:
            raise ValueError("contract_id required")

        result = {
            "id": contract_id,
            "contract_id": contract_id,
            "status": "active",
            "activated_at": datetime.utcnow().isoformat()
        }

        route_event(
            event_type="DECISION_ZYRA",
            payload=result,
            source="CONTRACTS_SERVICE"
        )

        return result

    # ========================================================
    # TERMINATE CONTRACT
    # ========================================================

    def terminate_contract(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        contract_id = payload.get("contract_id")

        if not contract_id:
            raise ValueError("contract_id required")

        result = {
            "id": contract_id,
            "contract_id": contract_id,
            "status": "terminated",
            "terminated_at": datetime.utcnow().isoformat()
        }

        route_event(
            event_type="DECISION_ZYRA",
            payload=result,
            source="CONTRACTS_SERVICE"
        )

        ledger_record(
            evento="CONTRACT_TERMINATED",
            estado="OK",
            payload={"contract_id": contract_id},
            origen="CONTRACTS_SERVICE"
        )

        return result
