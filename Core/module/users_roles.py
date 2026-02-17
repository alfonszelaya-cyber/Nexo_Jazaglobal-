# ============================================================
# users_roles.py
# NEXO / ZYRA — USUARIOS & ROLES (NEGOCIO)
# ROLE ENGINE — ENTERPRISE READY
# ============================================================

from datetime import datetime, timezone
import uuid

# ============================================================
# UTILIDAD TIEMPO
# ============================================================

def _now():
    return datetime.now(timezone.utc).isoformat()


# ============================================================
# ROLES BASE DEL SISTEMA
# ============================================================

ROLES = {
    "ADMIN": {
        "description": "Administrador del negocio",
        "permissions": ["ALL"]
    },
    "MANAGER": {
        "description": "Gestión operativa",
        "permissions": ["VIEW_REPORTS", "APPROVE_PAYMENTS"]
    },
    "OPERATOR": {
        "description": "Operación diaria",
        "permissions": ["CREATE_SALES", "VIEW_OWN"]
    }
}


# ============================================================
# REGISTER ROLE IN CORE
# ============================================================

def register_role_in_core(role_name: str, permissions: list) -> dict:

    role_id = str(uuid.uuid4())

    return {
        "role_id": role_id,
        "role_name": role_name,
        "permissions": permissions,
        "status": "CREATED",
        "created_at": _now()
    }


# ============================================================
# ASSIGN ROLE TO USER
# ============================================================

def assign_role_in_core(user_id: str, role_id: str) -> dict:

    return {
        "user_id": user_id,
        "role_id": role_id,
        "assigned_at": _now(),
        "status": "ASSIGNED"
    }


# ============================================================
# LIST ROLES
# ============================================================

def list_roles_in_core() -> dict:

    roles_list = []

    for name, data in ROLES.items():
        roles_list.append({
            "role_id": str(uuid.uuid4()),
            "role_name": name,
            "description": data["description"],
            "permissions": data["permissions"],
            "status": "ACTIVE",
            "loaded_at": _now()
        })

    return {
        "total_roles": len(roles_list),
        "roles": roles_list,
        "listed_at": _now()
    }


# ============================================================
# VALIDATE PERMISSION
# ============================================================

def validate_permission(role_name: str, permission: str) -> bool:

    role = ROLES.get(role_name)

    if not role:
        return False

    if "ALL" in role["permissions"]:
        return True

    return permission in role["permissions"]


# ============================================================
# UPDATE ROLE STATUS
# ============================================================

def update_role_status_in_core(role_id: str, new_status: str) -> dict:

    return {
        "role_id": role_id,
        "new_status": new_status,
        "updated_at": _now()
    }
