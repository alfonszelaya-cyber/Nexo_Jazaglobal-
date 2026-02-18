# ============================================================
# ZYRA / NEXO
# USERS SERVICE — CLEAN STABLE
# ============================================================

from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user_model import User
from datetime import datetime


class UsersService:

    # ========================================================
    # STATUS
    # ========================================================

    def get_status(self):
        return {
            "service": "IDENTITY_SERVICE",
            "status": "active",
            "timestamp": datetime.utcnow()
        }

    # ========================================================
    # CREATE USER
    # ========================================================

    def create_user(self, data):
        db: Session = SessionLocal()

        try:
            new_user = User(
                username=data.username,
                email=data.email,
                password_hash=data.password,
                is_active=True,
                created_at=datetime.utcnow()
            )

            db.add(new_user)
            db.commit()
            db.refresh(new_user)

            return {
                "user_id": str(new_user.id),
                "username": new_user.username,
                "email": new_user.email,
                "roles": data.roles if data.roles else [],
                "status": "ACTIVE
