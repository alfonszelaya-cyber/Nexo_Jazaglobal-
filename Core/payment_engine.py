# ============================================================
# payment_engine.py
# Motor de pagos del CORE ZYRA/NEXO
# ============================================================

import os
import json
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

PAYMENTS_FILE = os.path.join(DATA_DIR, "payments.json")

# -----------------------------
# Registro de pagos
# -----------------------------
def add_payment(payment: dict):
    """
    Registra un pago en el sistema
    """
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payment_record = {"payment": payment, "ts": ts}

    try:
        if os.path.exists(PAYMENTS_FILE):
            with open(PAYMENTS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        else:
            data = []
    except Exception:
        data = []

    data.append(payment_record)

    try:
        with open(PAYMENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[PAYMENT_ENGINE] Error al guardar pago: {e}")

def get_all_payments():
    """
    Retorna todos los pagos registrados
    """
    try:
        with open(PAYMENTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []
    return data

def get_payment_summary():
    """
    Devuelve resumen de pagos
    """
    payments = get_all_payments()
    total = sum(p["payment"].get("amount", 0) for p in payments)
    print(f"[PAYMENT_ENGINE] Total pagos: {total}, registros: {len(payments)}")
    return {"total": total, "count": len(payments)}