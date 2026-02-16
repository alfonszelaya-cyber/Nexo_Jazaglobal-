# ============================================================
# ZYRA / NEXO
# AUTH SERVICE — ENTERPRISE 3.0
# Identity & Access Logic Layer
# ============================================================

import uuid
from datetime import datetime, timedelta
from typing import Dict, Any

# ============================================================
# CORE / MODULE / INFRA IMPORTS (READY FOR EXPANSION)
# ============================================================

# Ledger
from Core.core_ledger import ledger_record

# Event Router
from infrastructure.events.event_router import route_event

# Payload Validator
from domain.services.payload_validator import validate_payload


class AuthServices:
    """
    Enterprise Authentication Services

    - Can emit events to CORE
    - Can register ledger entries
    - Can validate payloads
    - Ready to connect to modules or templates
    """

    TOKEN_EXP_MINUTES = 60

    # ========================================================
    # LOGIN
    # ========================================================

    def login(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        validate_payload(payload)

        email = payload.get("email")
        if not email:
            raise ValueError("Email is required")

        token = uuid.uuid4().hex
        issued_at = datetime.utcnow()
        expires_at = issued_at + timedelta(minutes=self.TOKEN_EXP_MINUTES)

        result = {
            "user": email,
            "access_token": token,
            "token_type": "bearer",
            "expires_in_minutes": self.TOKEN_EXP_MINUTES,
            "issued_at": issued_at,
            "expires_at": expires_at
        }

        # ------------------------------------------------------
        # Emit Event to CORE
        # ------------------------------------------------------

        route_event(
            event_type="LOGIN",
            payload=result,
            source="AUTH_SERVICE"
        )

        # ------------------------------------------------------
        # Register Ledger Entry
        # ------------------------------------------------------

        ledger_record(
            evento="USER_LOGIN",
            estado="OK",
            payload={"user": email},
            origen="AUTH_SERVICE"
        )

        return result

    # ========================================================
    # VALIDATE TOKEN
    # ========================================================

    def validate_token(self, token: str) -> Dict[str, Any]:

        if not token:
            raise ValueError("Invalid token")

        response = {
            "access_granted": True,
            "validated_at": datetime.utcnow()
        }

        route_event(
            event_type="TOKEN_VALIDATED",
            payload=response,
            source="AUTH_SERVICE"
        )

        return response

    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self, email: str) -> Dict[str, Any]:

        result = {
            "user": email,
            "status": "session_closed",
            "timestamp": datetime.utcnow()
        }

        route_event(
            event_type="LOGOUT",
            payload=result,
            source="AUTH_SERVICE"
        )

        ledger_record(
            evento="USER_LOGOUT",
            estado="OK",
            payload={"user": email},
            origen="AUTH_SERVICE"
        )

        return result
