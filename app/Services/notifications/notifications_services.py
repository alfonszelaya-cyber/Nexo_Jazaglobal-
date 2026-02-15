# ============================================================
# ZYRA / NEXO
# NOTIFICATIONS SERVICE — ENTERPRISE 3.0
# Notification Dispatch Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.module.module_events import register_notification_event
from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class NotificationsService:
    """
    Enterprise Notification Service

    - Registers notification inside Core module
    - Emits system-wide events
    - Writes immutable ledger trace
    """

    # ========================================================
    # SEND NOTIFICATION
    # ========================================================

    def send_notification(self, user_id: str, message: str) -> Dict[str, Any]:

        if not user_id:
            raise ValueError("User ID required")

        if not message:
            raise ValueError("Message cannot be empty")

        notification_id = str(uuid.uuid4())

        result = {
            "notification_id": notification_id,
            "user_id": user_id,
            "message": message,
            "status": "sent",
            "sent_at": datetime.utcnow()
        }

        # Core registration
        register_notification_event(result)

        # Emit system event
        route_event(
            event_type="NOTIFICATION_SENT",
            payload=result,
            source="NOTIFICATIONS_SERVICE"
        )

        # Ledger immutable trace
        ledger_record(
            evento="NOTIFICATION_SENT",
            estado="SUCCESS",
            payload=result,
            origen="NOTIFICATIONS_SERVICE"
        )

        return result

    # ========================================================
    # MARK AS READ
    # ========================================================

    def mark_as_read(self, notification_id: str) -> Dict[str, Any]:

        if not notification_id:
            raise ValueError("Notification ID required")

        result = {
            "notification_id": notification_id,
            "status": "read",
            "read_at": datetime.utcnow()
        }

        # Emit system event
        route_event(
            event_type="NOTIFICATION_READ",
            payload=result,
            source="NOTIFICATIONS_SERVICE"
        )

        # Ledger immutable trace
        ledger_record(
            evento="NOTIFICATION_READ",
            estado="SUCCESS",
            payload=result,
            origen="NOTIFICATIONS_SERVICE"
        )

        return result
