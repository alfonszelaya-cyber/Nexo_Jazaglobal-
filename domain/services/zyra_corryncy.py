# =====================================================
# NEXO / ZYRA — CONVERSIÓN EN TIEMPO REAL SEGÚN CLIENTE
# =====================================================

import requests
from decimal import Decimal, ROUND_HALF_UP
import json
import time
from pathlib import Path

# Archivo de historial de conversiones
HISTORIAL_FILE = Path("zyra_conversion_history.json")

# Cache temporal para tasas de cambio
CACHE_TTL = 300  # segundos
_currency_cache = {}
_cache_timestamp = 0

# ================= FUNCIONES =======================

def obtener_cliente(cliente_id):
    """Simulado: devuelve preferencia de moneda del cliente"""
    dummy = {
        1: {"nombre": "Cliente A", "pais": "GT", "moneda_pref": "GTQ"},
        2: {"nombre": "Cliente B", "pais": "CN", "moneda_pref": "CNY"},
        3: {"nombre": "Cliente C", "pais": "US", "moneda_pref": "USD"},
        4: {"nombre": "Cliente D", "pais": "JP", "moneda_pref": "JPY"},
    }
    return dummy.get(cliente_id, {"nombre": f"Cliente {cliente_id}", "moneda_pref": "USD"})

def fetch_exchange_rates():
    """Trae tasas de cambio en tiempo real (FIAT y CRYPTO)"""
    global _currency_cache, _cache_timestamp
    if time.time() - _cache_timestamp < CACHE_TTL and _currency_cache:
        return _currency_cache

    rates = {}
    try:
        # FIAT
        fiat_data = requests.get("https://api.exchangerate.host/latest?base=USD").json()
        for cur, val in fiat_data.get("rates", {}).items():
            rates[cur.upper()] = Decimal(val)

        # CRYPTO
        crypto_ids = {"BTC": "bitcoin", "ETH": "ethereum", "USDT": "tether"}
        crypto_data = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=" +
            ",".join(crypto_ids.values()) + "&vs_currencies=usd"
        ).json()
        for k, v in crypto_ids.items():
            rates[k] = Decimal(crypto_data[v]["usd"])

    except Exception as e:
        print("[ERROR] No se pudo obtener tasas:", e)
        # fallback 1:1
        for cur in ["USD", "GTQ", "CNY", "JPY", "BTC", "ETH", "USDT"]:
            rates[cur] = Decimal(1)

    _currency_cache = rates
    _cache_timestamp = time.time()
    return rates

def convert(amount: float, from_currency: str, to_currency: str) -> Decimal:
    """Convierte al instante cualquier moneda a la preferida del cliente"""
    rates = fetch_exchange_rates()
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates or to_currency not in rates:
        raise ValueError(f"Moneda no soportada: {from_currency} -> {to_currency}")

    # Conversión usando USD como base interna
    usd_amount = Decimal(amount) / rates[from_currency]
    result = usd_amount * rates[to_currency]

    # Redondeo según moneda
    if to_currency in ["BTC", "ETH", "USDT"]:
        return result.quantize(Decimal("0.00000001"), ROUND_HALF_UP)
    return result.quantize(Decimal("0.01"), ROUND_HALF_UP)

def procesar_pago(cliente_id: int, monto: float, moneda_origen: str):
    """Convierte al instante según moneda preferida del cliente"""
    cliente = obtener_cliente(cliente_id)
    moneda_destino = cliente.get("moneda_pref", "USD")
    convertido = convert(monto, moneda_origen, moneda_destino)

    # Registro en historial
    historial = []
    if HISTORIAL_FILE.exists():
        try:
            with open(HISTORIAL_FILE, "r") as f:
                historial = json.load(f)
        except json.JSONDecodeError:
            historial = []

    historial.append({
        "cliente_id": cliente_id,
        "from": moneda_origen,
        "to": moneda_destino,
        "amount": str(convertido),
        "timestamp": time.time()
    })

    with open(HISTORIAL_FILE, "w") as f:
        json.dump(historial, f, indent=2)

    return convertido, moneda_destino

# ================= EJEMPLO =========================

if __name__ == "__main__":
    pagos = [
        {"cliente_id": 1, "monto": 1000, "moneda_origen": "USD"},
        {"cliente_id": 2, "monto": 500, "moneda_origen": "USD"},
        {"cliente_id": 3, "monto": 0.05, "moneda_origen": "BTC"},
        {"cliente_id": 4, "monto": 300, "moneda_origen": "USD"},
    ]

    for pago in pagos:
        convertido, moneda_destino = procesar_pago(
            pago["cliente_id"], pago["monto"], pago["moneda_origen"]
        )
        cliente = obtener_cliente(pago["cliente_id"])["nombre"]
        print(f"{cliente}: {pago['monto']} {pago['moneda_origen']} => {convertido} {moneda_destino}")