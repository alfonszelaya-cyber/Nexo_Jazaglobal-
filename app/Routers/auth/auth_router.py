# ============================================================
# AUTH SERVICE — ENTERPRISE 3.1 (STABLE PROTECTED BUILD)
# ============================================================

import uuid
from datetime import datetime, timedelta
from typing import Dict, Any

from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class AuthServices:

    TOKEN_EXP_MINUTES = 60

    # ========================================================
    # LOGIN
    # ========================================================

    def login(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        email = payload.get("email")
        password = payload.get("password")

        if not email or not password:
            raise ValueError("Email and password required")

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

        # 🔒 PROTECCIÓN: si event_router falla, NO rompe login
        try:
            route_event(
                event_type="LOGIN",
                payload=result,
                source="AUTH_SERVICE"
            )
        except Exception as e:
            print("route_event error:", e)

        # 🔒 PROTECCIÓN: si ledger falla, NO rompe login
        try:
            ledger_record(
                evento="USER_LOGIN",
                estado="OK",
                payload={"user": email},
                origen="AUTH_SERVICE"
            )
        except Exception as e:
            print("ledger_record error:", e)

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

        try:
            route_event(
                event_type="TOKEN_VALIDATED",
                payload=response,
                source="AUTH_SERVICE"
            )
        except Exception as e:
            print("route_event error:", e)

        return response

    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self, email: str) -> Dict[str, Any]:

        if not email:
            raise ValueError("User required")

        result = {
            "user": email,
            "status": "session_closed",
            "timestamp": datetime.utcnow()
        }

        try:
            route_event(
                event_type="LOGOUT",
                payload=result,
                source="AUTH_SERVICE"
            )
        except Exception as e:
            print("route_event error:", e)

        try:
            ledger_record(
                evento="USER_LOGOUT",
                estado="OK",
                payload={"user": email},
                origen="AUTH_SERVICE"
            )
        except Exception as e:
            print("ledger_record error:", e)

        return result
