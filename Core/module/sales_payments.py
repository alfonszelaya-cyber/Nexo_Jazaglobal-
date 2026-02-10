# sales_payments.py
# NEXO / ZYRA — VENTAS / POS
# PAGOS DE VENTA
# PASIVO | EVENT-DRIVEN

from datetime import datetime, timezone

def register_payment(payload: dict) -> dict:
    """
    Registra un pago asociado a una venta (sin persistir).
    """
    return {
        "sale_id": payload.get("sale_id"),
        "payment_id": payload.get("payment_id"),
        "method": payload.get("method"),
        "amount": payload.get("amount", 0),
        "currency": payload.get("currency", "USD"),
        "status": "PAID",
        "ts": datetime.now(timezone.utc).isoformat()
    }