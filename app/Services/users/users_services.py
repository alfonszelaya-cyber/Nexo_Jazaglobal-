# ============================================================
# ZYRA / NEXO
# USERS SERVICE — ENTERPRISE 3.0
# Business Logic & Database Persistence
# ============================================================

from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user_model import User
from datetime import datetime


class UsersService:

    def __init__(self):
        self.db: Session = SessionLocal()

    # ========================================================
    # STATUS
    # ========================================================

    def get_status(self):
        return {
            "module": "IDENTITY_SERVICE",
            "status": "active",
            "version": "3.0",
            "timestamp": datetime.utcnow()
        }

    # ========================================================
    # CREATE USER
    # ========================================================

    def create_user(self, data):
        try:
            new_user = User(
                username=data.username,
                email=data.email,
                password_hash=data.password,  # 🔥 CORREGIDO
                is_active=True,
                created_at=datetime.utcnow()
            )

            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)

            return {
                "user_id": new_user.id,
                "username": new_user.username,
                "email": new_user.email,
                "roles": data.roles if data.roles else [],
                "status": "ACTIVE",
                "created_at": new_user.created_at
            }

        except Exception as e:
            self.db.rollback()
            raise e

        finally:
            self.db.close()

    # ========================================================
    # GET USER
    # ========================================================

    def get_user(self, payload):
        try:
            user = self.db.query(User).filter(
                User.id == payload.user_id
            ).first()

            if not user:
                return None

            return {
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "roles": [],
                "status": "ACTIVE" if user.is_active else "INACTIVE",
                "created_at": user.created_at
            }

        finally:
            self.db.close()

    # ========================================================
    # UPDATE USER
    # ========================================================

    def update_user(self, payload):
        try:
            user = self.db.query(User).filter(
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

            if payload.new_status:
                user.is_active = payload.new_status.upper() == "ACTIVE"

            self.db.commit()

            return {
                "user_id": user.id,
                "action": "UPDATE",
                "status": "SUCCESS",
                "executed_at": datetime.utcnow()
            }

        finally:
            self.db.close()

    # ========================================================
    # DELETE USER
    # ========================================================

    def delete_user(self, payload):
        try:
            user = self.db.query(User).filter(
                User.id == payload.user_id
            ).first()

            if not user:
                return {
                    "user_id": payload.user_id,
                    "action": "DELETE",
                    "status": "NOT_FOUND",
                    "executed_at": datetime.utcnow()
                }

            self.db.delete(user)
            self.db.commit()

            return {
                "user_id": payload.user_id,
                "action": "DELETE",
                "status": "SUCCESS",
                "executed_at": datetime.utcnow()
            }

        finally:
            self.db.close()
