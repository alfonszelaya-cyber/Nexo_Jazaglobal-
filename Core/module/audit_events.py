# ==========================================================
# audit_events.py
# NEXO / ZYRA — AUDITORÍA & TRAZABILIDAD
# PASIVO | SOLO EMITE
# ==========================================================

from infrastructure.events.emit_events import emit_events


def emit_audit_event(event_name: str, payload: dict):
    emit_events("core", {
        "module": "AUDITORIA",
        "event": event_name,
        "payload": payload
    })
