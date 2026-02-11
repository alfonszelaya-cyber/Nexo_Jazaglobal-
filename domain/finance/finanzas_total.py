# ============================================================
# finanzas_total.py
# NEXO / ZYRA — MOTOR FINANCIERO GLOBAL
# Domain Layer | Agregador Maestro | 10+ Years Architecture
# ============================================================

import json
import os
import uuid
from datetime import datetime
from typing import Dict, List


# ============================================================
# CONFIGURACIÓN BASE (Domain Safe — sin rutas hardcodeadas externas)
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORTS_DIR = os.path.join(BASE_DIR, "reportes_financieros")

os.makedirs(REPORTS_DIR, exist_ok=True)


# ============================================================
# TASAS DE CAMBIO (Preparado para futura integración API)
# ============================================================

def obtener_tasas_cambio() -> Dict[str, float]:
    """
    Simulación de tasas.
    En producción: conectar con servicio externo (infra layer).
    """
    return {
        "CNY": 7.24,
        "BTC": 0.000018,
        "GTQ": 7.82,
        "MXN": 17.10,
    }


# ============================================================
# LECTURA SEGURA DE JSON
# ============================================================

def _leer_archivo_json(ruta: str) -> List[dict]:
    if not os.path.exists(ruta):
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []


# ============================================================
# MOTOR PRINCIPAL
# ============================================================

def generar_reporte_maestro() -> dict:
    print("\n🚀 [ZYRA FINANCE CORE] Procesando balance global...")

    tasas = obtener_tasas_cambio()

    metricas = {
        "ingresos": 0.0,
        "inversion": 0.0,
        "impuestos": 0.0,
    }

    mapeo = {
        "ingresos": [
            "e_invoices.json",
            "universal_payments.json",
            "ledger.json",
        ],
        "inversion": [
            "inventory.json",
            "ledger_finanzas.json",
            "fiscal_documents.json",
        ],
        "impuestos": [
            "tax_declarations.json",
            "documentos_fiscales.json",
        ],
    }

    # ========================================================
    # AGREGACIÓN FINANCIERA
    # ========================================================

    for categoria, archivos in mapeo.items():
        for archivo in archivos:
            ruta = os.path.join(DATA_DIR, archivo)
            registros = _leer_archivo_json(ruta)

            for reg in registros:
                monto = (
                    reg.get("monto")
                    or reg.get("monto_usd")
                    or reg.get("monto_base")
                    or 0.0
                )
                try:
                    metricas[categoria] += float(monto)
                except (ValueError, TypeError):
                    continue

    ingresos = metricas["ingresos"]
    inversion = metricas["inversion"]
    impuestos = metricas["impuestos"]

    ganancia_neta = ingresos - inversion - impuestos

    # ========================================================
    # TIEMPOS
    # ========================================================

    ahora = datetime.utcnow()
    fecha = ahora.strftime("%Y-%m-%d")
    mes = ahora.strftime("%Y-%m")
    anio = ahora.strftime("%Y")

    # ========================================================
    # REPORTE FINAL
    # ========================================================

    reporte_final = {
        "id_reporte": str(uuid.uuid4()),
        "timestamp_utc": ahora.isoformat(),
        "fecha": fecha,
        "mes": mes,
        "anio": anio,
        "metricas": {
            "ingresos": round(ingresos, 2),
            "inversion": round(inversion, 2),
            "impuestos": round(impuestos, 2),
            "ganancia_neta": round(ganancia_neta, 2),
        },
        "conversiones": {
            moneda: round(ganancia_neta * tasa, 8)
            for moneda, tasa in tasas.items()
        },
    }

    # ========================================================
    # PERSISTENCIA HISTÓRICA
    # ========================================================

    for tipo, nombre in [
        ("diario", fecha),
        ("mensual", mes),
        ("anual", anio),
    ]:
        archivo_reporte = os.path.join(
            REPORTS_DIR, f"reporte_{tipo}_{nombre}.json"
        )

        historial = _leer_archivo_json(archivo_reporte)
        historial.append(reporte_final)

        with open(archivo_reporte, "w", encoding="utf-8") as f:
            json.dump(historial, f, indent=2)

    print("📂 Reportes financieros actualizados correctamente.")
    return reporte_final


# ============================================================
# EJECUCIÓN LOCAL CONTROLADA
# ============================================================

if __name__ == "__main__":
    generar_reporte_maestro()
