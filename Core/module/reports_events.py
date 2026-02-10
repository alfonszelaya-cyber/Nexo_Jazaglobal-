# ============================================================
# reports_events.py
# NEXO / ZYRA — REPORTES & BI
# EVENTOS DE REPORTES
# PASIVO | SOLO EMITE
# ============================================================

from emit_event import emit_event

def emit_report_event(event_name: str, payload: dict):
    emit_event("business", {
        "module": "REPORTS",
        "event": event_name,
        "payload": payload
    })