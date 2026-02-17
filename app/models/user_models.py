# ============================================================
# ZYRA / NEXO
# USER MODEL — ENTERPRISE 3.0
# SQLAlchemy ORM Model
# ============================================================

import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class User(Base):
    """
    Tabla real de usuarios del sistema.
    """

    __tablename__ = "users"

    # ========================================================
    # PRIMARY KEY
    # ========================================================

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    # ========================================================
    # USER FIELDS
    # ========================================================

    username: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    email: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        unique=True,
        index=True
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
