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
                "success": True,
                "message": "Usuario creado correctamente",
                "user_id": str(new_user.id)
            }

        except Exception as e:
            db.rollback()
            return {
                "success": False,
                "message": str(e),
                "user_id": ""
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
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "password": user.password_hash,
                "roles": [],
                "is_active": user.is_active,
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
                    "success": False,
                    "message": "Usuario no encontrado"
                }

            if payload.username:
                user.username = payload.username

            if payload.email:
                user.email = payload.email

            if payload.password:
                user.password_hash = payload.password

            if payload.is_active is not None:
                user.is_active = payload.is_active

            db.commit()

            return {
                "success": True,
                "message": "Usuario actualizado correctamente"
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
                    "success": False,
                    "message": "Usuario no encontrado"
                }

            db.delete(user)
            db.commit()

            return {
                "success": True,
                "message": "Usuario eliminado correctamente"
            }

        finally:
            db.close()
