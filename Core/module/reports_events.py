# ============================================================
# reports_events.py
# NEXO / ZYRA — REPORTES & BI
# EVENTOS DE REPORTES
# PASIVO | SOLO EMITE
# ============================================================

from infrastructure.events.emit_events import emit_events

def emit_report_event(event_name: str, payload: dict):
    emit_event("business", {
        "module": "REPORTS",
        "event": event_name,
        "payload": payload
    })
