# ============================================================
# AUTH SERVICE — ENTERPRISE 3.1 (FULL ACTIVE — JSON SAFE)
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

        # 🔒 FIX REAL: datetime → string ISO (JSON SAFE)
        issued_at_iso = issued_at.isoformat()
        expires_at_iso = expires_at.isoformat()

        result = {
            "id": token,  # requerido por event_router
            "user": email,
            "access_token": token,
            "token_type": "bearer",
            "expires_in_minutes": self.TOKEN_EXP_MINUTES,
            "issued_at": issued_at_iso,
            "expires_at": expires_at_iso
        }

        # 🔹 Evento válido del catálogo
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

        validated_at = datetime.utcnow().isoformat()

        response = {
            "id": token,
            "access_granted": True,
            "validated_at": validated_at
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

        timestamp = datetime.utcnow().isoformat()

        result = {
            "id": uuid.uuid4().hex,
            "user": email,
            "status": "session_closed",
            "timestamp": timestamp
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
