# ============================================================
# ZYRA / NEXO
# OPERATIONS SERVICE — ENTERPRISE 3.0
# Core Operations Execution Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.module.module_events import register_operation_event
from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class OperationsService:
    """
    Enterprise Operations Service

    - Executes business operations
    - Registers event inside Core
    - Emits infrastructure event
    - Writes immutable ledger trace
    """

    # ========================================================
    # EXECUTE OPERATION
    # ========================================================

    def execute_operation(self, operation_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:

        if not operation_type:
            raise ValueError("Operation type required")

        operation_id = str(uuid.uuid4())

        result = {
            "operation_id": operation_id,
            "type": operation_type,
            "payload": payload,
            "status": "executed",
            "executed_at": datetime.utcnow()
        }

        # Register inside Core module
        register_operation_event(result)

        # Emit system-wide event
        route_event(
            event_type="OPERATION_EXECUTED",
            payload=result,
            source="OPERATIONS_SERVICE"
        )

        # Ledger immutable trace
        ledger_record(
            evento="OPERATION_EXECUTED",
            estado="SUCCESS",
            payload=result,
            origen="OPERATIONS_SERVICE"
        )

        return result

    # ========================================================
    # GET OPERATION STATUS
    # ========================================================

    def get_operation_status(self, operation_id: str) -> Dict[str, Any]:

        if not operation_id:
            raise ValueError("Operation ID required")

        result = {
            "operation_id": operation_id,
            "status": "completed",
            "checked_at": datetime.utcnow()
        }

        # Ledger trace (read audit)
        ledger_record(
            evento="OPERATION_STATUS_CHECK",
            estado="INFO",
            payload=result,
            origen="OPERATIONS_SERVICE"
        )

        return result
