# ============================================================
# ZYRA / NEXO
# ROLES SERVICE — ENTERPRISE 3.0
# Role & Permission Management Logic
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, List


class RolesService:

    @staticmethod
    def create_role(role_name: str, permissions: List[str]) -> Dict:

        return {
            "role_id": str(uuid.uuid4()),
            "role_name": role_name,
            "permissions": permissions,
            "created_at": datetime.utcnow()
        }

    @staticmethod
    def assign_role(user_id: str, role_id: str) -> Dict:

        return {
            "user_id": user_id,
            "role_id": role_id,
            "status": "assigned",
            "assigned_at": datetime.utcnow()
        }
