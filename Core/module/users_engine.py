# ============================================================
# users_engine.py
# NEXO / ZYRA — USUARIOS & ROLES (NEGOCIO)
# MOTOR DE USUARIOS
# PASIVO | SIN SEGURIDAD CORE | SIN AUTOEJECUCIÓN
# ============================================================

from datetime import datetime, timezone

def create_user(payload: dict) -> dict:
    """
    Crea un usuario de negocio (no identidad core).
    """
    return {
        "user_id": payload.get("user_id"),
        "name": payload.get("name"),
        "email": payload.get("email"),
        "role": payload.get("role"),
        "status": "ACTIVE",
        "ts": datetime.now(timezone.utc).isoformat()
    }