# ============================================================
# ledger_events.py
# NEXO / ZYRA — CONTABILIDAD / LEDGER
# EVENTOS CONTABLES
# PASIVO | SOLO EMITE
# ============================================================

from emit_event import emit_event

def emit_ledger_event(event_name: str, payload: dict):
    emit_event("business", {
        "module": "LEDGER",
        "event": event_name,
        "payload": payload
    })