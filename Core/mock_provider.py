# ============================================================
# mock_provider.py
# Proveedor simulado para CORE ZYRA/NEXO
# ============================================================

from datetime import datetime
import random

# -----------------------------
# Registro interno de operaciones simuladas
# -----------------------------
_mock_records = []

# -----------------------------
# Funciones de simulación
# -----------------------------
def simulate_payment(amount: float, currency: str = "USD"):
    """
    Simula un pago y devuelve resultado
    """
    status = random.choice(["SUCCESS", "FAILED"])
    record = {
        "operation": "payment",
        "amount": amount,
        "currency": currency,
        "status": status,
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    _mock_records.append(record)
    return record


def simulate_order(order_id: str, total: float):
    """
    Simula una orden de compra o venta
    """
    status = random.choice(["CONFIRMED", "REJECTED", "PENDING"])
    record = {
        "operation": "order",
        "order_id": order_id,
        "total": total,
        "status": status,
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    _mock_records.append(record)
    return record


def list_mock_records():
    """
    Lista todas las operaciones simuladas
    """
    return _mock_records