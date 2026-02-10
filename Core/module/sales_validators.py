# sales_validators.py
# NEXO / ZYRA — VENTAS / POS
# VALIDADORES DE VENTA
# PASIVO

def validate_sale(payload: dict) -> bool:
    required = ["sale_id", "customer_id", "items", "total"]

    for key in required:
        if key not in payload:
            return False

    if not isinstance(payload.get("items"), list):
        return False

    if payload.get("total", 0) < 0:
        return False

    return True