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
        # El servicio maneja su propia conexión de forma profesional
        self.db: Session = SessionLocal()

    def get_status(self):
        """Verifica que el servicio de identidad esté online."""
        return {
            "service": "IDENTITY_SERVICE",
            "status": "active",
            "timestamp": datetime.utcnow()
        }

    def create_user(self, data):
        """
        Crea un usuario de forma automática desde el payload del router.
        Recibe el objeto 'data' (CreateUserRequest) completo.
        """
        try:
            # Creamos la instancia del modelo usando los datos del usuario real
            new_user = User(
                username=data.username,
                email=data.email,
                password=data.password,  # Aquí se guarda la clave
                roles=data.roles if hasattr(data, 'roles') else "user",
                is_active=True,
                created_at=datetime.utcnow()
            )

            # Persistencia en la base de datos de JAZA
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

    def get_user(self, payload):
        """Busca un usuario por su ID o Email."""
        user = self.db.query(User).filter(
            (User.id == payload.user_id) | (User.email == payload.email)
        ).first()
        
        if not user:
            return {"error": "Usuario no encontrado"}
        return user

    def update_user(self, payload):
        """Actualiza la información de un usuario existente."""
        user = self.db.query(User).filter(User.id == payload.user_id).first()
        if user:
            for key, value in payload.dict(exclude_unset=True).items():
                setattr(user, key, value)
            self.db.commit()
            return {"success": True, "message": "Usuario actualizado"}
        return {"success": False, "message": "Usuario no encontrado"}

    def delete_user(self, payload):
        """Elimina un usuario del sistema."""
        user = self.db.query(User).filter(User.id == payload.user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return {"success": True, "message": "Usuario eliminado"}
        return {"success": False, "message": "Usuario no encontrado"}
