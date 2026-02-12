# ============================================================
# integrations_events.py
# NEXO / ZYRA — INTEGRACIONES EXTERNAS
# EVENTOS DE INTEGRACIÓN
# PASIVO | SOLO EMITE
# ============================================================

from infrastructure.events.emit_events import emit_event

def emit_integration_event(event_name: str, payload: dict):
    emit_event("business", {
        "module": "INTEGRATIONS",
        "event": event_name,
        "payload": payload
    })
