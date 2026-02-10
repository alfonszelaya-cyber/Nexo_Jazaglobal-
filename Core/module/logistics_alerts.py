# logistics_alerts.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# ALERTAS Y RIESGOS LOGÍSTICOS
# PASIVO | ZYRA-COMPATIBLE

def evaluate_logistics_alerts(payload: dict) -> dict:
    """
    Evalúa riesgos y genera alertas lógicas.
    """
    alerts = []

    if payload.get("delay_days", 0) > 3:
        alerts.append("RETRASO_CRITICO")

    if payload.get("customs_block", False):
        alerts.append("BLOQUEO_ADUANA")

    return {
        "shipment_id": payload.get("shipment_id"),
        "alerts": alerts,
        "risk_level": "ALTO" if alerts else "NORMAL"
    }