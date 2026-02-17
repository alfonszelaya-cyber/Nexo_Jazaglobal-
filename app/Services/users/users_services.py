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
        # Conexión profesional por instancia
        self.db: Session = SessionLocal()

    # ========================================================
    # STATUS
    # ========================================================

    def get_status(self):
        """Verifica que el servicio de identidad esté online."""
        return {
            "service": "IDENTITY_SERVICE",
            "status": "active",
            "timestamp": datetime.utcnow()
        }

    # ========================================================
    # CREATE USER
    # ========================================================

    def create_user(self, data):
        """
        Crea un usuario desde el payload del router.
        Recibe el objeto CreateUserRequest completo.
        """
        try:
            new_user = User(
                username=data.username,
                email=data.email,
                password=data.password,
                roles=data.roles if hasattr(data, "roles") else "user",
                is_active=True,
                created_at=datetime.utcnow()
            )

            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)

            return {
                "success": True,
                "message": f"Usuario {new_user.username} creado exitosamente",
                "user_id": new_user.id
            }

        except Exception as e:
            self.db.rollback()
            return {
                "success": False,
                "message": f"Error al crear usuario: {str(e)}"
            }

        finally:
            self.db.close()

    # ========================================================
    # GET USER
    # ========================================================

    def get_user(self, payload):
        """Busca un usuario por ID o Email."""
        try:
            user = self.db.query(User).filter(
                (User.id == payload.user_id) |
                (User.email == payload.email)
            ).first()

            if not user:
                return {"success": False, "message": "Usuario no encontrado"}

            return user

        finally:
            self.db.close()

    # ========================================================
    # UPDATE USER
    # ========================================================

    def update_user(self, payload):
        """Actualiza información de un usuario."""
        try:
            user = self.db.query(User).filter(
                User.id == payload.user_id
            ).first()

            if not user:
                return {"success": False, "message": "Usuario no encontrado"}

            for key, value in payload.dict(exclude_unset=True).items():
                setattr(user, key, value)

            self.db.commit()

            return {
                "success": True,
                "message": "Usuario actualizado"
            }

        finally:
            self.db.close()

    # ========================================================
    # DELETE USER
    # ========================================================

    def delete_user(self, payload):
        """Elimina un usuario del sistema."""
        try:
            user = self.db.query(User).filter(
                User.id == payload.user_id
            ).first()

            if not user:
                return {"success": False, "message": "Usuario no encontrado"}

            self.db.delete(user)
            self.db.commit()

            return {
                "success": True,
                "message": "Usuario eliminado"
            }

        finally:
            self.db.close()
