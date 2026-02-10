# ============================================================
# pos_engine.py
# Motor POS del CORE ZYRA/NEXO
# ============================================================

from datetime import datetime

# -----------------------------
# Registro interno de transacciones
# -----------------------------
_pos_transactions = []

# -----------------------------
# Funciones POS
# -----------------------------
def register_sale(sale_id: str, amount: float, currency: str = "USD", metadata: dict = None):
    """
    Registra una venta en el POS
    """
    record = {
        "sale_id": sale_id,
        "amount": amount,
        "currency": currency,
        "metadata": metadata or {},
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    _pos_transactions.append(record)
    return record

def get_sales_summary():
    """
    Devuelve resumen de ventas
    """
    total_sales = sum(r["amount"] for r in _pos_transactions)
    summary = {
        "total_sales": total_sales,
        "num_transactions": len(_pos_transactions)
    }
    return summary

def list_sales():
    """
    Lista todas las ventas registradas
    """
    return _pos_transactions