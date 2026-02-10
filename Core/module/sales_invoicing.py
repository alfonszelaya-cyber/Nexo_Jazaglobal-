# sales_invoicing.py
# NEXO / ZYRA — VENTAS / POS
# FACTURACIÓN
# PASIVO | EVENT-DRIVEN

from datetime import datetime, timezone

def generate_invoice(payload: dict) -> dict:
    """
    Genera datos base de factura (sin persistir).
    """
    return {
        "invoice_id": payload.get("invoice_id"),
        "sale_id": payload.get("sale_id"),
        "customer_id": payload.get("customer_id"),
        "items": payload.get("items", []),
        "subtotal": payload.get("subtotal", 0),
        "taxes": payload.get("taxes", 0),
        "total": payload.get("total", 0),
        "currency": payload.get("currency", "USD"),
        "status": "ISSUED",
        "ts": datetime.now(timezone.utc).isoformat()
    }