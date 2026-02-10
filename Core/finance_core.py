# ============================================================
# finance_core.py
# NEXO / ZYRA — FINANCE CORE
# Conversión monetaria | Base financiera | Ledger-aware
# ============================================================

import os
import requests
from datetime import datetime
from zyra_ledger_hook import ledger_record

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

# -------------------------
# CONVERSIÓN DE MONEDAS
# -------------------------

def convert_currency(amount, from_currency, to_currency, country="GLOBAL"):
    from_currency = str(from_currency).upper()
    to_currency = str(to_currency).upper()

    # Misma moneda
    if from_currency == to_currency:
        return {
            "result": amount,
            "rate": 1.0,
            "from": from_currency,
            "to": to_currency,
            "ts": datetime.utcnow().isoformat()
        }

    # BTC ↔ USD
    if {"BTC", "USD"} == {from_currency, to_currency}:
        try:
            r = requests.get(
                COINGECKO_URL,
                params={"ids": "bitcoin", "vs_currencies": "usd"},
                timeout=10
            ).json()

            btc_usd = float(r["bitcoin"]["usd"])

            result = amount * btc_usd if from_currency == "BTC" else amount / btc_usd

            ledger_record(
                event="CONVERSION_MONEDA",
                status="OK",
                detail={
                    "from": from_currency,
                    "to": to_currency,
                    "amount": amount,
                    "rate": btc_usd,
                    "result": result
                }
            )

            return {
                "result": result,
                "rate": btc_usd,
                "from": from_currency,
                "to": to_currency,
                "ts": datetime.utcnow().isoformat()
            }

        except Exception as e:
            ledger_record(
                event="CONVERSION_MONEDA",
                status="ERROR",
                detail=str(e)
            )
            return {
                "error": "Fallo al consultar tasa BTC/USD",
                "from": from_currency,
                "to": to_currency
            }

    # Par no soportado
    return {
        "error": "Par de monedas no soportado",
        "from": from_currency,
        "to": to_currency,
        "country": country
    }

# ============================================================
# NOTAS
# - main puede importarlo sin ejecutar pruebas
# - No imprime nada en import
# - Ledger registra conversión
# - Compatible con Radar VIP y Finanzas
# ============================================================

if __name__ == "__main__":
    print(convert_currency(100, "USD", "BTC"))
    print(convert_currency(0.01, "BTC", "USD"))