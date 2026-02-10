# import_profitability_engine.py
# NEXO / ZYRA — IMPORTACIONES
# RENTABILIDAD
# PASIVO | EVENT-DRIVEN

def calculate_profitability(payload: dict) -> dict:
    """
    Calcula margen y retorno esperado.
    """
    costo = payload.get("costo_total", 0)
    precio = payload.get("precio_venta", 0)

    utilidad = precio - costo
    margen = (utilidad / costo) if costo else 0

    return {
        "import_id": payload.get("import_id"),
        "utilidad": utilidad,
        "margen": round(margen, 4)
    }