# sales_engine.py
# NEXO / ZYRA — VENTAS / POS
# MOTOR DE VENTAS
# PASIVO | EVENT-DRIVEN | SIN AUTOEJECUCIÓN

from datetime import datetime, timezone

def create_sale(payload: dict) -> dict:
    """
    Crea una venta base (sin persistir).
    """
    return {
        "sale_id": payload.get("sale_id"),
        "customer_id": payload.get("customer_id"),
        "items": payload.get("items", []),
        "total": payload.get("total", 0),
        "currency": payload.get("currency", "USD"),
        "status": "CREATED",
        "ts": datetime.now(timezone.utc).isoformat()
    }