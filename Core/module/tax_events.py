# ============================================================
# tax_events.py
# NEXO / ZYRA — FISCAL / IMPUESTOS
# EVENTOS FISCALES
# PASIVO | SOLO EMITE
# ============================================================

from infrastructure.events.emit_events import emit_events

def emit_tax_event(event_name: str, payload: dict):
    emit_event("business", {
        "module": "TAX",
        "event": event_name,
        "payload": payload
    })
