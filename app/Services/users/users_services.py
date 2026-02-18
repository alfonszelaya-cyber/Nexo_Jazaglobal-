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
                "status": "ACTIVE",
                "created_at": new_user.created_at
            }

        finally:
            db.close()

    # ========================================================
    # GET USER
    # ========================================================

    def get_user(self, payload):
        db: Session = SessionLocal()

        try:
            user = db.query(User).filter(
                User.id == payload.user_id
            ).first()

            if not user:
                return None

            return {
                "user_id": str(user.id),
                "username": user.username,
                "email": user.email,
                "roles": [],
                "status": "ACTIVE" if user.is_active else "INACTIVE",
                "created_at": user.created_at
            }

        finally:
            db.close()

    # ========================================================
    # UPDATE USER
    # ========================================================

    def update_user(self, payload):
        db: Session = SessionLocal()

        try:
            user = db.query(User).filter(
                User.id == payload.user_id
            ).first()

            if not user:
                return {
                    "user_id": payload.user_id,
                    "action": "UPDATE",
                    "status": "NOT_FOUND",
                    "executed_at": datetime.utcnow()
                }

            if payload.username:
                user.username = payload.username

            if payload.email:
                user.email = payload.email

            if payload.is_active is not None:
                user.is_active = payload.is_active

            db.commit()

            return {
                "user_id": str(user.id),
                "action": "UPDATE",
                "status": "SUCCESS",
                "executed_at": datetime.utcnow()
            }

        finally:
            db.close()

    # ========================================================
    # DELETE USER
    # ========================================================

    def delete_user(self, payload):
        db: Session = SessionLocal()

        try:
            user = db.query(User).filter(
                User.id == payload.user_id
            ).first()

            if not user:
                return {
                    "user_id": payload.user_id,
                    "action": "DELETE",
                    "status": "NOT_FOUND",
                    "executed_at": datetime.utcnow()
                }

            db.delete(user)
            db.commit()

            return {
                "user_id": payload.user_id,
                "action": "DELETE",
                "status": "SUCCESS",
                "executed_at": datetime.utcnow()
            }

        finally:
            db.close()
