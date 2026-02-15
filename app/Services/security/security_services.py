# ============================================================
# ZYRA / NEXO
# SECURITY SERVICE — ENTERPRISE 3.0
# Authentication & Authorization Logic Layer
# ============================================================

import uuid
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.module.users_engine import validate_user_credentials
from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class SecurityService:
    """
    Enterprise Security Service

    - Authenticates against Core
    - Emits security events
    - Writes immutable ledger trace
    - Ready for DB / Supabase integration
    """

    TOKEN_EXP_MINUTES = 60

    # ========================================================
    # AUTHENTICATE
    # ========================================================

    def authenticate(self, username: str, password: str) -> Dict[str, Any]:

        if not username or not password:
            raise ValueError("Username and password required")

        # Hash password (enterprise-ready structure)
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Validate against Core module
        is_valid = validate_user_credentials(username, password_hash)

        if not is_valid:
            raise ValueError("Invalid credentials")

        token = uuid.uuid4().hex

        result = {
            "user": username,
            "access_token": token,
            "token_type": "bearer",
            "expires_in_minutes": self.TOKEN_EXP_MINUTES,
            "issued_at": datetime.utcnow()
        }

        # Emit security event
        route_event(
            event_type="USER_AUTHENTICATED",
            payload={"user": username},
            source="SECURITY_SERVICE"
        )

        # Ledger trace
        ledger_record(
            evento="USER_AUTHENTICATED",
            estado="SUCCESS",
            payload={"user": username},
            origen="SECURITY_SERVICE"
        )

        return result

    # ========================================================
    # VALIDATE TOKEN
    # ========================================================

    def validate_token(self, token: str) -> Dict[str, Any]:

        if not token:
            raise ValueError("Token required")

        result = {
            "token": token,
            "valid": True,
            "validated_at": datetime.utcnow()
        }

        route_event(
            event_type="TOKEN_VALIDATED",
            payload={"token": token},
            source="SECURITY_SERVICE"
        )

        return result
