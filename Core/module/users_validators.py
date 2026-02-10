# ============================================================
# users_validators.py
# NEXO / ZYRA — USUARIOS & ROLES (NEGOCIO)
# VALIDADORES DE USUARIOS
# ============================================================

def validate_user(payload: dict) -> bool:
    required = [
        "user_id",
        "name",
        "email",
        "role"
    ]

    for key in required:
        if key not in payload:
            return False

    if "@" not in payload.get("email", ""):
        return False

    return True