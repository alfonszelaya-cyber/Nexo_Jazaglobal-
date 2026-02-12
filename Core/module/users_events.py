# ============================================================
# users_events.py
# NEXO / ZYRA — USUARIOS & ROLES (NEGOCIO)
# EVENTOS DE USUARIOS
# PASIVO | SOLO EMITE
# ============================================================

from infrastructure.events.emit_events import emit_events

def emit_user_event(event_name: str, payload: dict):
    emit_event("business", {
        "module": "USERS",
        "event": event_name,
        "payload": payload
    })
