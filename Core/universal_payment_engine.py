# ============================================================
# universal_payment_engine.py
# Motor universal de pagos global del CORE ZYRA
# Conversión automática entre monedas según pago y preferencia del cliente
# ============================================================

import os
import json
from datetime import datetime

# -----------------------------
# Configuración de archivo
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
PAYMENTS_FILE = os.path.join(DATA_DIR, "universal_payments.json")

# Inicializar archivo si no existe
if not os.path.exists(PAYMENTS_FILE):
    with open(PAYMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# -----------------------------
# Tipo de cambio base (USD y BTC de referencia)
# -----------------------------
EXCHANGE_RATES = {
    "USD": 1.0,       # Base USD
    "BTC": 30000.0,   # Ejemplo: 1 BTC = 30,000 USD
    "CNY": 0.14,      # 1 CNY ~ 0.14 USD
    "GTQ": 0.13,      # 1 GTQ ~ 0.13 USD
    "MXN": 0.05,      # 1 MXN ~ 0.05 USD
    "NIO": 0.027,     # 1 Córdoba ~ 0.027 USD
    # Se pueden añadir todas las monedas necesarias
}

# -----------------------------
# Funciones principales
# -----------------------------
def convert_currency(amount: float, from_currency: str, to_currency: str):
    """
    Convierte una cantidad entre monedas usando EXCHANGE_RATES
    """
    if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
        raise ValueError(f"Moneda no soportada: {from_currency} o {to_currency}")
    usd_amount = amount * EXCHANGE_RATES[from_currency]  # Convertir a USD
    converted = usd_amount / EXCHANGE_RATES[to_currency]
    return round(converted, 6)

def add_payment(client_id: str, amount: float, from_currency: str = "USD",
                to_currency: str = None, payment_method: str = "WIRE",
                country: str = None, remarks: str = ""):
    """
    Registra un pago internacional, convirtiendo a la moneda de preferencia del cliente.
    Si to_currency es None, se usa moneda local según país.
    """
    if to_currency is None:
        to_currency = get_currency_by_country(country) if country else "USD"

    converted_amount = convert_currency(amount, from_currency, to_currency)

    entry = {
        "client_id": client_id,
        "country": country,
        "amount_original": amount,
        "currency_original": from_currency,
        "amount_received": converted_amount,
        "currency_received": to_currency,
        "payment_method": payment_method,
        "remarks": remarks,
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    payments = load_payments()
    payments.append(entry)
    save_payments(payments)
    return entry

def get_currency_by_country(country: str):
    """
    Devuelve la moneda más común del país
    """
    country_currency_map = {
        "China": "CNY",
        "Guatemala": "GTQ",
        "México": "MXN",
        "Nicaragua": "NIO",
        "USA": "USD",
        "El Salvador": "USD",
        "Panamá": "USD",
    }
    return country_currency_map.get(country, "USD")

def load_payments():
    try:
        with open(PAYMENTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []
    return data

def save_payments(data):
    with open(PAYMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_all_payments():
    """
    Devuelve todos los pagos registrados
    """
    return load_payments()

def get_payments_by_client(client_id: str):
    """
    Devuelve los pagos filtrados por cliente
    """
    return [p for p in load_payments() if p.get("client_id") == client_id]