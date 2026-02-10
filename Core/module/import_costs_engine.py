# import_costs_engine.py
# NEXO / ZYRA — IMPORTACIONES
# CÁLCULO DE COSTOS
# PASIVO | EVENT-DRIVEN

def calculate_import_costs(payload: dict) -> dict:
    """
    Calcula costos totales de importación.
    """
    total = (
        payload.get("costo_producto", 0) +
        payload.get("flete", 0) +
        payload.get("seguro", 0) +
        payload.get("aranceles", 0)
    )

    return {
        "import_id": payload.get("import_id"),
        "costo_total": total
    }