# ============================================================
# finanzas_total.py
# NEXO / ZYRA — REPORTE FINANCIERO GLOBAL
# CORE | LECTURA | AGREGADOR MAESTRO
# ============================================================

import json
import os
import uuid
from datetime import datetime

# ============================================================
# CONFIGURACIÓN DE RUTAS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORTS_DIR = os.path.join(BASE_DIR, "reportes_financieros")
os.makedirs(REPORTS_DIR, exist_ok=True)

# ============================================================
# TASAS (SIMULADAS)
# ============================================================

def obtener_tasas_cambio():
    return {
        "CNY": 7.24,
        "BTC": 0.000018,
        "GTQ": 7.82,
        "MXN": 17.10
    }

# ============================================================
# MOTOR PRINCIPAL
# ============================================================

def generar_reporte_maestro():
    print(f"\n🚀 [FINANZAS_TOTAL] Procesando balance global...")

    tasas = obtener_tasas_cambio()
    metricas = {"ingresos": 0.0, "inversion": 0.0, "impuestos": 0.0}

    mapeo = {
        "ingresos": ["e_invoices.json", "universal_payments.json", "ledger.json"],
        "inversion": ["inventory.json", "ledger_finanzas.json", "fiscal_documents.json"],
        "impuestos": ["tax_declarations.json", "documentos_fiscales.json"]
    }

    for categoria, archivos in mapeo.items():
        for archivo in archivos:
            ruta = os.path.join(DATA_DIR, archivo)
            if os.path.exists(ruta):
                try:
                    with open(ruta, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            for reg in data:
                                monto = (
                                    reg.get("monto") or
                                    reg.get("monto_usd") or
                                    reg.get("monto_base") or
                                    0.0
                                )
                                metricas[categoria] += float(monto)
                except Exception:
                    continue

    ingresos = metricas["ingresos"]
    inversion = metricas["inversion"]
    impuestos = metricas["impuestos"]
    ganancia_neta = ingresos - inversion - impuestos

    ahora = datetime.now()
    fecha_hoy = ahora.strftime("%Y-%m-%d")
    mes_actual = ahora.strftime("%Y-%m")
    anio_actual = ahora.strftime("%Y")

    print("\n" + "═"*60)
    print("        REPORTE FINANCIERO JAZA GLOBAL SYSTEMS")
    print(f"        FECHA: {fecha_hoy} | HORA: {ahora.strftime('%H:%M:%S')}")
    print("═"*60)
    print(f" [+] INVERSIÓN TOTAL:   $ {inversion:,.2f} USD")
    print(f" [+] INGRESOS BRUTOS:  $ {ingresos:,.2f} USD")
    print(f" [+] IMPUESTOS:        $ {impuestos:,.2f} USD")
    print(" " + "─"*56)

    simbolo = "✅" if ganancia_neta >= 0 else "🚨"
    label = "GANANCIA TOTAL" if ganancia_neta >= 0 else "PÉRDIDA TOTAL"
    print(f" {simbolo} {label}:  $ {ganancia_neta:,.2f} USD")

    print("\n🌐 CONVERSIÓN GLOBAL:")
    print(f"  └─ CNY: ¥ {ganancia_neta * tasas['CNY']:,.2f}")
    print(f"  └─ GTQ: Q {ganancia_neta * tasas['GTQ']:,.2f}")
    print(f"  └─ BTC: ₿ {ganancia_neta * tasas['BTC']:.8f}")
    print("═"*60)

    reporte_final = {
        "id_reporte": str(uuid.uuid4())[:8],
        "fecha": fecha_hoy,
        "mes": mes_actual,
        "anio": anio_actual,
        "usd_balance": round(ganancia_neta, 2),
        "inversion": round(inversion, 2),
        "detalles_divisas": {
            "CNY": round(ganancia_neta * tasas["CNY"], 2),
            "GTQ": round(ganancia_neta * tasas["GTQ"], 2),
            "BTC": round(ganancia_neta * tasas["BTC"], 8)
        }
    }

    for tipo, nombre in [("diario", fecha_hoy), ("mensual", mes_actual), ("anual", anio_actual)]:
        archivo_rep = os.path.join(REPORTS_DIR, f"reporte_{tipo}_{nombre}.json")
        historial = []

        if os.path.exists(archivo_rep):
            try:
                with open(archivo_rep, "r", encoding="utf-8") as f:
                    historial = json.load(f)
            except Exception:
                historial = []

        historial.append(reporte_final)

        with open(archivo_rep, "w", encoding="utf-8") as f:
            json.dump(historial, f, indent=2)

    print("📂 Reportes guardados en /reportes_financieros/")


# ============================================================
# PRUEBA LOCAL
# ============================================================

if __name__ == "__main__":
    generar_reporte_maestro()