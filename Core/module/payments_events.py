# ============================================================
# payments_events.py
# NEXO / ZYRA — PAGOS & BANCOS
# EVENTOS DE PAGOS
# PASIVO | SOLO EMITE
# ============================================================

from emit_event import emit_event

def emit_payment_event(event_name: str, payload: dict):
    emit_event("business", {
        "module": "PAYMENTS",
        "event": event_name,
        "payload": payload
    })