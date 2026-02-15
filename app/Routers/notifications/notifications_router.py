# ============================================================
# ZYRA / NEXO
# NOTIFICATIONS ROUTER — ENTERPRISE 3.0
# Alerts & Communication Layer
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.notifications_schema import (
    NotificationsStatusResponse,
    SendNotificationRequest,
    SendNotificationResponse,
    ListNotificationsRequest,
    ListNotificationsResponse,
    MarkAsReadRequest,
    MarkAsReadResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.notifications_services import NotificationsService


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

notifications_service = NotificationsService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=NotificationsStatusResponse)
def notifications_status():
    return NotificationsStatusResponse(
        module="ZYRA_NOTIFICATIONS_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# SEND NOTIFICATION
# ============================================================

@router.post("/send", response_model=SendNotificationResponse)
def send_notification(payload: SendNotificationRequest):
    try:
        return notifications_service.send_notification(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# LIST NOTIFICATIONS
# ============================================================

@router.post("/list", response_model=ListNotificationsResponse)
def list_notifications(payload: ListNotificationsRequest):
    return notifications_service.list_notifications(payload)


# ============================================================
# MARK AS READ
# ============================================================

@router.post("/mark-read", response_model=MarkAsReadResponse)
def mark_as_read(payload: MarkAsReadRequest):
    return notifications_service.mark_as_read(payload)
