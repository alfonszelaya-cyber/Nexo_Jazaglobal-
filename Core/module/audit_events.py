# audit_events.py
# NEXO / ZYRA — AUDITORÍA & TRAZABILIDAD
# EVENTOS DE AUDITORÍA
# PASIVO | SOLO EMITE

from emit_event import emit_event

def emit_audit_event(event_name: str, payload: dict):
    emit_event("core", {
        "module": "AUDITORIA",
        "event": event_name,
        "payload": payload
    })