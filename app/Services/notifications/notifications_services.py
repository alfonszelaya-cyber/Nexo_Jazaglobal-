# ============================================================
# ZYRA / NEXO
# NOTIFICATIONS SERVICE — ENTERPRISE 3.0
# Notification Dispatch Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict


class NotificationsService:

    @staticmethod
    def send_notification(user_id: str, message: str) -> Dict:

        return {
            "notification_id": str(uuid.uuid4()),
            "user_id": user_id,
            "message": message,
            "status": "sent",
            "sent_at": datetime.utcnow()
        }

    @staticmethod
    def mark_as_read(notification_id: str) -> Dict:

        return {
            "notification_id": notification_id,
            "status": "read",
            "read_at": datetime.utcnow()
        }
