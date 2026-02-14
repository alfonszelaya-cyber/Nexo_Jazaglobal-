# ============================================================
# ledger_events.py
# NEXO / ZYRA — CONTABILIDAD / LEDGER
# EVENTOS CONTABLES
# PASIVO | SOLO EMITE
# ============================================================

from infrastructure.events.emit_events import emit_events

def emit_ledger_event(event_name: str, payload: dict):
    emit_events("business", {
        "module": "LEDGER",
        "events": events_name,
        "payload": payload
    })
