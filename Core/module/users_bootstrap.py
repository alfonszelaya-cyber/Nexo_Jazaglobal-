# ============================================================
# users_bootstrap.py
# NEXO / ZYRA — USUARIOS & ROLES (NEGOCIO)
# BOOTSTRAP OFICIAL DEL MÓDULO
# NO TOCA CORE | AUTO-REGISTRO PASIVO
# ============================================================

def bootstrap_users():
    return {
        "module": "USERS",
        "status": "READY",
        "components": [
            "users_engine",
            "users_roles",
            "users_events",
            "users_validators",
            "users_health"
        ]
    }


# Auto-registro único
USERS_MODULE = bootstrap_users()