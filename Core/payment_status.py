# ============================================================
# payment_status.py
# Gestión de estados de pagos del CORE ZYRA/NEXO
# ============================================================

from datetime import datetime

# -----------------------------
# Estados posibles
# -----------------------------
STATUSES = ["PENDING", "COMPLETED", "FAILED", "CANCELLED"]

# -----------------------------
# Registro de pagos (simulado)
# -----------------------------
_payment_records = []

# -----------------------------
# Funciones de estado
# -----------------------------
def add_payment_record(payment_id: str, amount: float, currency: str, status: str = "PENDING"):
    """
    Agrega un pago al registro con estado inicial
    """
    if status not in STATUSES:
        raise ValueError(f"Estado inválido: {status}")
    record = {
        "payment_id": payment_id,
        "amount": amount,
        "currency": currency,
        "status": status,
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    _payment_records.append(record)
    return record

def update_payment_status(payment_id: str, new_status: str):
    """
    Actualiza el estado de un pago existente
    """
    if new_status not in STATUSES:
        raise ValueError(f"Estado inválido: {new_status}")
    for rec in _payment_records:
        if rec["payment_id"] == payment_id:
            rec["status"] = new_status
            rec["ts"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return rec
    raise ValueError(f"No se encontró pago con ID: {payment_id}")

def get_payment_status(payment_id: str):
    """
    Devuelve el estado actual de un pago
    """
    for rec in _payment_records:
        if rec["payment_id"] == payment_id:
            return rec["status"]
    return None

def list_all_payments():
    """
    Devuelve todos los pagos registrados
    """
    return _payment_records