# sales_events.py
# NEXO / ZYRA — VENTAS / POS
# EVENTOS DE VENTAS
# PASIVO | SOLO EMITE

from infrastructure.events.emit_events import emit_events

def emit_sales_event(event_name: str, payload: dict):
    emit_event("business", {
        "module": "SALES",
        "event": event_name,
        "payload": payload
    })
