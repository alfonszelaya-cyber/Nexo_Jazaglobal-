# ============================================================
# payments_engine.py
# NEXO / ZYRA — PAGOS & BANCOS
# MOTOR DE PAGOS
# PASIVO | EVENT-DRIVEN | SIN AUTOEJECUCIÓN
# ============================================================

from datetime import datetime, timezone

def create_payment(payload: dict) -> dict:
    """
    Crea un pago base (sin persistir).
    """
    return {
        "payment_id": payload.get("payment_id"),
        "source": payload.get("source"),          # cash / bank / gateway
        "reference": payload.get("reference"),    # sale_id / invoice_id
        "amount": payload.get("amount", 0),
        "currency": payload.get("currency", "USD"),
        "method": payload.get("method"),          # card / transfer / cash
        "status": "INITIATED",
        "ts": datetime.now(timezone.utc).isoformat()
    }