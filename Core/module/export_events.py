# ============================================================
# export_events.py
# NEXO / ZYRA — EXPORT EVENTS
# ============================================================

from emit_event import emit_event

def export_event(event: str, payload: dict):
    emit_event("module", {
        "module": "export",
        "event": event,
        "payload": payload
    })