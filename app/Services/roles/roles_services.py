# ============================================================
# ZYRA / NEXO
# ROLES SERVICE — ENTERPRISE 3.0
# Role & Permission Management Logic
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, List, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.module.users_roles import register_role_in_core, assign_role_in_core
from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class RolesService:
    """
    Enterprise Roles Service

    - Registers roles inside Core
    - Assigns roles through Core logic
    - Emits events
    - Writes immutable ledger trace
    """

    # ========================================================
    # CREATE ROLE
    # ========================================================

    def create_role(self, role_name: str, permissions: List[str]) -> Dict[str, Any]:

        if not role_name:
            raise ValueError("Role name required")

        role_id = str(uuid.uuid4())

        # Register inside Core module
        register_role_in_core(role_id, role_name, permissions)

        result = {
            "role_id": role_id,
            "role_name": role_name,
            "permissions": permissions,
            "created_at": datetime.utcnow()
        }

        # Emit event
        route_event(
            event_type="ROLE_CREATED",
            payload=result,
            source="ROLES_SERVICE"
        )

        # Ledger trace
        ledger_record(
            evento="ROLE_CREATED",
            estado="SUCCESS",
            payload=result,
            origen="ROLES_SERVICE"
        )

        return result

    # ========================================================
    # ASSIGN ROLE
    # ========================================================

    def assign_role(self, user_id: str, role_id: str) -> Dict[str, Any]:

        if not user_id or not role_id:
            raise ValueError("User ID and Role ID required")

        # Assign inside Core module
        assign_role_in_core(user_id, role_id)

        result = {
            "user_id": user_id,
            "role_id": role_id,
            "status": "assigned",
            "assigned_at": datetime.utcnow()
        }

        # Emit event
        route_event(
            event_type="ROLE_ASSIGNED",
            payload=result,
            source="ROLES_SERVICE"
        )

        # Ledger trace
        ledger_record(
            evento="ROLE_ASSIGNED",
            estado="SUCCESS",
            payload=result,
            origen="ROLES_SERVICE"
        )

        return result
