# ============================================================
# compliance_events.py
# NEXO / ZYRA — COMPLIANCE / REGULACIÓN
# EVENTOS DE CUMPLIMIENTO
# PASIVO | SOLO EMITE
# ============================================================

from emit_event import emit_event

def emit_compliance_event(event_name: str, payload: dict):
    emit_event("business", {
        "module": "COMPLIANCE",
        "event": event_name,
        "payload": payload
    })