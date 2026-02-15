# ============================================================
# ZYRA / NEXO
# USERS SERVICE — ENTERPRISE 3.0
# User Management Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any, List

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.module.users_engine import register_user_core
from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class UsersService:
    """
    Enterprise Users Service

    - Registers users through Core
    - Emits system events
    - Writes immutable ledger traces
    """

    # ========================================================
    # CREATE USER
    # ========================================================

    def create_user(self, username: str, email: str) -> Dict[str, Any]:

        if not username or not email:
            raise ValueError("Username and email required")

        user_id = str(uuid.uuid4())

        # Call Core module
        register_user_core(user_id, username, email)

        result = {
            "user_id": user_id,
            "username": username,
            "email": email,
            "status": "created",
            "created_at": datetime.utcnow()
        }

        # Emit event
        route_event(
            event_type="USER_CREATED",
            payload=result,
            source="USERS_SERVICE"
        )

        # Ledger trace
        ledger_record(
            evento="USER_CREATED",
            estado="SUCCESS",
            payload=result,
            origen="USERS_SERVICE"
        )

        return result

    # ========================================================
    # GET USER
    # ========================================================

    def get_user(self, user_id: str) -> Dict[str, Any]:

        if not user_id:
            raise ValueError("User ID required")

        result = {
            "user_id": user_id,
            "status": "active",
            "retrieved_at": datetime.utcnow()
        }

        return result

    # ========================================================
    # LIST USERS
    # ========================================================

    def list_users(self) -> Dict[str, Any]:

        result = {
            "total": 0,
            "users": [],
            "generated_at": datetime.utcnow()
        }

        return result
