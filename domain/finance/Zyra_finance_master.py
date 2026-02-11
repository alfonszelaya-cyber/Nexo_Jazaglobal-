import json
import os
import uuid
from datetime import datetime

# ==========================================
# Rutas base del sistema
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORTS_DIR = os.path.join(BASE_DIR, "reportes_financieros")

# ==========================================
# Reporte maestro financiero global
# ==========================================

def generar_reporte_maestro():

    print("\n🚀 [ZYRA FINANCE] Procesando balance global...")

    # Tasas de cambio base (mock controlado)
    tasas = {
        "CNY": 7.24,
        "BTC": 0.000018,
        "GTQ": 7.82
    }

    ingresos = 0.0
    inversion = 0.0
    impuestos = 0.0

    # --------------------------------------
    # Lectura universal de archivos financieros
    # --------------------------------------
    try:
        for archivo in os.listdir(DATA_DIR):
            if not archivo.endswith(".json"):
                continue

            ruta = os.path.join(DATA_DIR, archivo)

            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    data = json.load(f)

                    if not isinstance(data, list):
                        continue

                    for r in data:
                        monto = (
                            r.get("monto")
                            or r.get("monto_usd")
                            or 0.0
                        )

                        if "invoice" in archivo:
                            ingresos += float(monto)
                        elif "tax" in archivo:
                            impuestos += float(monto)
                        else:
                            inversion += float(monto)

            except Exception:
                pass

    except Exception:
        print("⚠️ No se pudo acceder a la carpeta DATA")

    # --------------------------------------
    # Cálculo final
    # --------------------------------------
    ganancia = ingresos - inversion - impuestos

    print("\n" + "═" * 60)
    print(f" GANANCIA TOTAL: $ {ganancia:,.2f} USD")
    print(
        f" CNY: ¥ {ganancia * tasas['CNY']:,.2f} | "
        f"GTQ: Q {ganancia * tasas['GTQ']:,.2f}"
    )
    print("═" * 60)