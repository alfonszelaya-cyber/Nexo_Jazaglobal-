# ============================================================
# AUTH SERVICE — ENTERPRISE 3.0 (FULL ACTIVE — STABLE FIX)
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
            "id": token,  # requerido por event_router para ref_id
            "user": email,
            "access_token": token,
            "token_type": "bearer",
            "expires_in_minutes": self.TOKEN_EXP_MINUTES,
            "issued_at": issued_at,
            "expires_at": expires_at
        }

        # 🔹 USAMOS EVENTO VÁLIDO DEL CATÁLOGO
        route_event(
            event_type="ALERTA_ZYRA",
            payload=result,
            source="AUTH_SERVICE"
        )

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
            "id": token,
            "access_granted": True,
            "validated_at": datetime.utcnow()
        }

        route_event(
            event_type="ALERTA_ZYRA",
            payload=response,
            source="AUTH_SERVICE"
        )

        return response

    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self, email: str) -> Dict[str, Any]:

        if not email:
            raise ValueError("User required")

        result = {
            "id": uuid.uuid4().hex,
            "user": email,
            "status": "session_closed",
            "timestamp": datetime.utcnow()
        }

        route_event(
            event_type="ALERTA_ZYRA",
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
