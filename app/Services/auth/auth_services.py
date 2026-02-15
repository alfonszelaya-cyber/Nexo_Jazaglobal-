# ============================================================
# ZYRA / NEXO
# AUTH SERVICE — ENTERPRISE 3.0
# Identity & Access Logic Layer
# ============================================================

import uuid
from datetime import datetime, timedelta
from typing import Dict


class AuthService:

    TOKEN_EXP_MINUTES = 60

    @staticmethod
    def login(email: str) -> Dict:
        """
        Simulated login process.
        """

        return {
            "user": email,
            "access_token": uuid.uuid4().hex,
            "token_type": "bearer",
            "expires_in_minutes": AuthService.TOKEN_EXP_MINUTES,
            "issued_at": datetime.utcnow()
        }

    @staticmethod
    def validate_token(token: str) -> Dict:
        """
        Simulated token validation.
        """

        if not token:
            raise ValueError("Invalid token")

        return {
            "access_granted": True,
            "validated_at": datetime.utcnow()
        }
