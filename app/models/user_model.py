# ============================================================
# ZYRA / NEXO
# USER MODEL — STABLE ENTERPRISE VERSION
# File: app/models/user_model.py
# ============================================================

import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    """
    Tabla real de usuarios del sistema.
    Sin roles físicos (roles se manejan lógico por ahora).
    Compatible con:
    - UsersService actual
    - UsersSchema estable
    - PostgreSQL Render
    """

    __tablename__ = "users"

    # ========================================================
    # PRIMARY KEY
    # ========================================================

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    # ========================================================
    # BASIC FIELDS
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
