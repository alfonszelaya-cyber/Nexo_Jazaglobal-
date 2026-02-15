# ============================================================
# ZYRA / NEXO
# SYSTEM SERVICE — ENTERPRISE 3.0
# Core System State & Health Logic
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.root_controller import system_state_update
from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class SystemService:
    """
    Enterprise System Service

    - Controls system state
    - Emits system events
    - Writes immutable ledger traces
    - Ready for production orchestration
    """

    # ========================================================
    # GET SYSTEM STATUS
    # ========================================================

    def get_system_status(self) -> Dict[str, Any]:

        result = {
            "system": "ZYRA_NEXO_CORE",
            "status": "running",
            "version": "3.0.0",
            "timestamp": datetime.utcnow()
        }

        return result

    # ========================================================
    # HEALTH CHECK
    # ========================================================

    def health_check(self) -> Dict[str, Any]:

        result = {
            "health_id": str(uuid.uuid4()),
            "status": "healthy",
            "checked_at": datetime.utcnow()
        }

        route_event(
            event_type="SYSTEM_HEALTH_CHECK",
            payload=result,
            source="SYSTEM_SERVICE"
        )

        ledger_record(
            evento="SYSTEM_HEALTH_CHECK",
            estado="OK",
            payload=result,
            origen="SYSTEM_SERVICE"
        )

        return result

    # ========================================================
    # SHUTDOWN REQUEST
    # ========================================================

    def shutdown_request(self, reason: str) -> Dict[str, Any]:

        if not reason:
            raise ValueError("Shutdown reason required")

        result = {
            "shutdown_id": str(uuid.uuid4()),
            "reason": reason,
            "status": "requested",
            "requested_at": datetime.utcnow()
        }

        # Update system state in Core
        system_state_update("SHUTDOWN_REQUESTED")

        route_event(
            event_type="SYSTEM_SHUTDOWN_REQUEST",
            payload=result,
            source="SYSTEM_SERVICE"
        )

        ledger_record(
            evento="SYSTEM_SHUTDOWN_REQUEST",
            estado="REQUESTED",
            payload=result,
            origen="SYSTEM_SERVICE"
        )

        return result
