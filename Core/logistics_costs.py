# ============================================================
# logistics_costs.py
# NEXO / ZYRA — MOTOR DE COSTOS LOGÍSTICOS GLOBAL
# Multi-país | Multi-transporte | Largo plazo (10+ años)
# PASIVO | SIN EFECTOS | CORE SAFE
# ============================================================

import os
from datetime import datetime

# ============================
# CONFIGURACIÓN BASE
# ============================

TRANSPORT_TYPES = ("MARITIMO", "AEREO", "TERRESTRE", "MULTIMODAL")

# ============================
# UTILIDAD TIEMPO
# ============================

def _now():
    return datetime.utcnow().isoformat()

# ============================
# CÁLCULO BASE
# ============================

def calculate_logistics_costs(payload: dict) -> dict:
    """
    Calcula costos totales de logística de forma estructurada.

    payload esperado:
    {
        "shipment_id": str,
        "transport_type": "MARITIMO|AEREO|TERRESTRE|MULTIMODAL",
        "flete": float,
        "seguro": float,
        "arancel": float,
        "combustible": float,
        "aduana": float,
        "almacenaje": float,
        "demoras": float,
        "otros": float,
        "riesgo": "BAJO|MEDIO|ALTO"
    }
    """

    transport_type = payload.get("transport_type", "DESCONOCIDO")

    costos = {
        "flete": payload.get("flete", 0),
        "seguro": payload.get("seguro", 0),
        "arancel": payload.get("arancel", 0),
        "combustible": payload.get("combustible", 0),
        "aduana": payload.get("aduana", 0),
        "almacenaje": payload.get("almacenaje", 0),
        "demoras": payload.get("demoras", 0),
        "otros": payload.get("otros", 0),
    }

    subtotal = sum(costos.values())

    riesgo = payload.get("riesgo", "BAJO")
    factor_riesgo = _risk_factor(riesgo)

    total = round(subtotal * factor_riesgo, 2)

    return {
        "shipment_id": payload.get("shipment_id"),
        "transport_type": transport_type,
        "riesgo": riesgo,
        "factor_riesgo": factor_riesgo,
        "timestamp": _now(),
        "costs": costos,
        "subtotal": subtotal,
        "total": total
    }

# ============================
# FACTOR DE RIESGO
# ============================

def _risk_factor(riesgo: str) -> float:
    """
    Ajusta costos según nivel de riesgo
    """
    if riesgo == "ALTO":
        return 1.25
    elif riesgo == "MEDIO":
        return 1.10
    return 1.00

# ============================
# SIMULADOR DE ESCENARIOS
# ============================

def simulate_scenarios(base_payload: dict, escenarios: list) -> list:
    """
    Ejecuta múltiples escenarios logísticos

    escenarios = [
        {"riesgo": "ALTO", "demoras": 500},
        {"riesgo": "MEDIO", "combustible": 300}
    ]
    """
    resultados = []

    for esc in escenarios:
        sim = base_payload.copy()
        sim.update(esc)
        resultados.append(calculate_logistics_costs(sim))

    return resultados

# ============================
# VALIDACIÓN BÁSICA
# ============================

def validate_payload(payload: dict) -> dict:
    """
    Valida estructura mínima del payload
    """
    errores = []

    if "shipment_id" not in payload:
        errores.append("shipment_id requerido")

    if payload.get("transport_type") not in TRANSPORT_TYPES:
        errores.append("transport_type inválido")

    return {
        "valid": len(errores) == 0,
        "errors": errores
    }

# ============================
# PROYECCIÓN FUTURA (10 AÑOS)
# ============================

def project_future_cost(current_cost: float, years: int = 10, inflation_rate: float = 0.05) -> float:
    """
    Proyecta costo logístico a futuro (inflación logística)
    """
    projected = current_cost
    for _ in range(years):
        projected *= (1 + inflation_rate)
    return round(projected, 2)

# ============================
# INDICADORES ESTRATÉGICOS
# ============================

def logistics_kpis(result: dict) -> dict:
    """
    Genera KPIs básicos de logística
    """
    total = result.get("total", 0)
    flete = result["costs"].get("flete", 0)

    return {
        "costo_total": total,
        "peso_flete_pct": round((flete / total) * 100, 2) if total else 0,
        "riesgo": result.get("riesgo"),
        "tipo_transporte": result.get("transport_type")
    }