# ============================================================
# users_engine.py
# NEXO / ZYRA — USUARIOS & ROLES (NEGOCIO)
# USER ENGINE — ENTERPRISE READY
# ============================================================

from datetime import datetime, timezone
import uuid
import hashlib

# ============================================================
# UTILIDAD TIEMPO
# ============================================================

def _now():
    return datetime.now(timezone.utc).isoformat()


# ============================================================
# HASH SIMPLE (PLACEHOLDER ENTERPRISE)
# ============================================================

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# ============================================================
# CREATE USER
# ============================================================

def create_user(payload: dict) -> dict:

    user_id = payload.get("user_id") or str(uuid.uuid4())

    return {
        "user_id": user_id,
        "name": payload.get("name"),
        "email": payload.get("email"),
        "role": payload.get("role"),
        "password_hash": _hash_password(payload.get("password", "123456")),
        "status": "ACTIVE",
        "created_at": _now()
    }


# ============================================================
# VALIDATE USER CREDENTIALS  🔥 (LO QUE FALTABA)
# ============================================================

def validate_user_credentials(email: str, password: str) -> dict:

    # Simulación enterprise (en producción va DB)
    fake_user = {
        "user_id": str(uuid.uuid4()),
        "email": email,
        "role": "ADMIN",
        "password_hash": _hash_password(password)
    }

    if _hash_password(password) == fake_user["password_hash"]:
        return {
            "valid": True,
            "user_id": fake_user["user_id"],
            "role": fake_user["role"],
            "validated_at": _now()
        }

    return {
        "valid": False,
        "validated_at": _now()
    }


# ============================================================
# GET USER
# ============================================================

def get_user_in_core(user_id: str) -> dict:

    return {
        "user_id": user_id,
        "name": "Demo User",
        "email": "demo@nexo.com",
        "role": "ADMIN",
        "status": "ACTIVE",
        "fetched_at": _now()
    }


# ============================================================
# UPDATE USER STATUS
# ============================================================

def update_user_status_in_core(user_id: str, new_status: str) -> dict:

    return {
        "user_id": user_id,
        "new_status": new_status,
        "updated_at": _now()
    }


# ============================================================
# DELETE USER
# ============================================================

def delete_user_in_core(user_id: str) -> dict:

    return {
        "user_id": user_id,
        "status": "DELETED",
        "deleted_at": _now()
    }


# ============================================================
# LIST USERS
# ============================================================

def list_users_in_core() -> dict:

    users = [
        {
            "user_id": str(uuid.uuid4()),
            "name": "Admin",
            "email": "admin@nexo.com",
            "role": "ADMIN",
            "status": "ACTIVE"
        }
    ]

    return {
        "total": len(users),
        "users": users,
        "listed_at": _now()
    }
