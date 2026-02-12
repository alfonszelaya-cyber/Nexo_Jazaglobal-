# =========================================
# tax_declarations.py
# NEXO / ZYRA — MOTOR DE DECLARACIONES FISCALES
# País-aware | Contador-friendly | Event-driven ready
# =========================================

import os
import json
from datetime import datetime
from domain.finance.accounting_engine import libro_por_empresa
from Core.core import ledger_record

# -------------------------
# RUTAS BASE
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

DECLARATIONS_DIR = os.path.join(DATA_DIR, "declarations")
os.makedirs(DECLARATIONS_DIR, exist_ok=True)

# -------------------------
# UTILIDADES
# -------------------------
def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def _now():
    return datetime.now().isoformat()

# -------------------------
# ACUMULADOS CONTABLES
# -------------------------
def calcular_acumulados(empresa_id, mes=None, anio=None):
    """
    Calcula ingresos, gastos y utilidad desde el libro contable
    """
    libro = libro_por_empresa(empresa_id)
    total_ingresos = 0.0
    total_gastos = 0.0

    for a in libro:
        fecha = datetime.fromisoformat(a["ts"])

        if mes and fecha.month != mes:
            continue
        if anio and fecha.year != anio:
            continue

        if a.get("credito") == "INGRESOS":
            total_ingresos += a.get("monto", 0)

        if a.get("debito") in ("GASTOS", "COSTOS"):
            total_gastos += a.get("monto", 0)

    return {
        "ingresos": round(total_ingresos, 2),
        "gastos": round(total_gastos, 2),
        "utilidad": round(total_ingresos - total_gastos, 2),
    }

# -------------------------
# DECLARACIÓN MENSUAL
# -------------------------
def generar_declaracion_mensual(empresa_id, pais, mes, anio):
    acumulados = calcular_acumulados(empresa_id, mes, anio)

    declaracion = {
        "empresa": empresa_id,
        "pais": pais,
        "tipo": "MENSUAL",
        "mes": mes,
        "anio": anio,
        "datos": acumulados,
        "estado": "BORRADOR",
        "generado": _now(),
    }

    fname = f"{empresa_id}_{pais}_{anio}_{mes}_mensual.json"
    path = os.path.join(DECLARATIONS_DIR, fname)
    _save(path, declaracion)

    ledger_record(
        event="DECLARACION_MENSUAL_GENERADA",
        status="BORRADOR",
        detail=declaracion
    )

    return declaracion

# -------------------------
# DECLARACIÓN ANUAL
# -------------------------
def generar_declaracion_anual(empresa_id, pais, anio):
    acumulados = calcular_acumulados(empresa_id, None, anio)

    declaracion = {
        "empresa": empresa_id,
        "pais": pais,
        "tipo": "ANUAL",
        "anio": anio,
        "datos": acumulados,
        "estado": "BORRADOR",
        "generado": _now(),
    }

    fname = f"{empresa_id}_{pais}_{anio}_anual.json"
    path = os.path.join(DECLARATIONS_DIR, fname)
    _save(path, declaracion)

    ledger_record(
        event="DECLARACION_ANUAL_GENERADA",
        status="BORRADOR",
        detail=declaracion
    )

    return declaracion
