# ============================================================
# users_roles.py
# NEXO / ZYRA — USUARIOS & ROLES (NEGOCIO)
# DEFINICIÓN DE ROLES DE NEGOCIO
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

def get_role(role_name: str) -> dict:
    return ROLES.get(role_name.upper(), {})