# ============================================================
# ZYRA / NEXO
# NOTIFICATIONS SCHEMA — ENTERPRISE 3.0
# System Alerts & Messaging Layer
# File: app/Schemas/notifications/notifications_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class NotificationsStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# SEND NOTIFICATION
# ============================================================

class SendNotificationRequest(BaseModel):
    user_id: str
    title: str
    message: str
    notification_type: str = Field(..., description="INFO | WARNING | CRITICAL")
    channel: str = Field(..., description="EMAIL | SMS | PUSH")


class SendNotificationResponse(BaseModel):
    notification_id: str
    user_id: str
    title: str
    message: str
    notification_type: str
    channel: str
    status: str  # SENT | FAILED | QUEUED
    created_at: datetime


# ============================================================
# LIST NOTIFICATIONS
# ============================================================

class ListNotificationsRequest(BaseModel):
    user_id: str


class NotificationItem(BaseModel):
    notification_id: str
    title: str
    message: str
    notification_type: str
    channel: str
    status: str
    created_at: datetime
    read_at: Optional[datetime] = None


class ListNotificationsResponse(BaseModel):
    user_id: str
    total: int
    notifications: List[NotificationItem]


# ============================================================
# MARK AS READ
# ============================================================

class MarkAsReadRequest(BaseModel):
    notification_id: str


class MarkAsReadResponse(BaseModel):
    notification_id: str
    status: str
    read_at: datetime
