# ============================================================
# ZYRA / NEXO
# NOTIFICATIONS SCHEMA — ENTERPRISE 3.0
# System Alerts & Messaging Layer
# ============================================================

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ============================================================
# CREATE NOTIFICATION
# ============================================================

class CreateNotificationRequest(BaseModel):
    user_id: str
    title: str
    message: str
    notification_type: str  # INFO | WARNING | CRITICAL
    channel: str  # EMAIL | SMS | PUSH


class NotificationResponse(BaseModel):
    notification_id: str
    user_id: str
    status: str  # SENT | FAILED | QUEUED
    created_at: datetime


# ============================================================
# MARK AS READ
# ============================================================

class MarkNotificationReadRequest(BaseModel):
    notification_id: str
    read_at: datetime
