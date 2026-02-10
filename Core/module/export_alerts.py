# ============================================================
# export_alerts.py
# NEXO / ZYRA — EXPORT ALERTS
# ============================================================

def check_export_alerts(status: dict) -> list:
    alerts = []

    if status.get("delay"):
        alerts.append("RETRASO EN EXPORTACIÓN")

    if status.get("customs_hold"):
        alerts.append("RETENIDO EN ADUANA")

    return alerts