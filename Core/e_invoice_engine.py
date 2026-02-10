# ============================================================
# e_invoice_engine.py
# Motor de facturación electrónica del CORE ZYRA/NEXO
# ============================================================

import os
import json
import datetime

# -----------------------------
# Configuración de facturas electrónicas
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
E_INVOICE_FILE = os.path.join(DATA_DIR, "e_invoices.json")
os.makedirs(DATA_DIR, exist_ok=True)

# Inicializar archivo si no existe
if not os.path.exists(E_INVOICE_FILE):
    with open(E_INVOICE_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# -----------------------------
# Funciones de facturación electrónica
# -----------------------------
def add_invoice(invoice: dict):
    """
    Agrega una factura electrónica
    """
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = {"invoice": invoice, "ts": ts}

    try:
        with open(E_INVOICE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []

    data.append(record)

    try:
        with open(E_INVOICE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

def get_all_invoices():
    """
    Retorna todas las facturas electrónicas
    """
    try:
        with open(E_INVOICE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except Exception:
        return []

def get_invoices_by_client(client_id: str):
    """
    Retorna todas las facturas de un cliente específico
    """
    all_invoices = get_all_invoices()
    return [inv for inv in all_invoices if inv.get("invoice", {}).get("client_id") == client_id]

def get_summary():
    """
    Retorna un resumen de facturación electrónica
    """
    all_invoices = get_all_invoices()
    summary = {
        "total_invoices": len(all_invoices),
        "total_amount": sum(inv.get("invoice", {}).get("amount", 0) for inv in all_invoices)
    }
    return summary