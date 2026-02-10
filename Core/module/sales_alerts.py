# sales_alerts.py
# NEXO / ZYRA — VENTAS / POS
# ALERTAS DE VENTAS
# PASIVO

def check_sales_alerts(payload: dict) -> list:
    alerts = []

    if payload.get("total", 0) == 0:
        alerts.append("VENTA_CON_TOTAL_CERO")

    if not payload.get("items"):
        alerts.append("VENTA_SIN_ITEMS")

    if payload.get("payment_status") == "FAILED":
        alerts.append("PAGO_FALLIDO")

    return alerts