# import_decision_engine.py
# NEXO / ZYRA — IMPORTACIONES
# DECISIÓN FINAL
# PASIVO | EVENT-DRIVEN

def evaluate_import(payload: dict) -> dict:
    """
    Decide si una importación es viable según margen.
    """
    margen = payload.get("margen", 0)
    minimo = payload.get("margen_minimo", 0.15)

    decision = "APROBADA" if margen >= minimo else "RECHAZADA"

    return {
        "import_id": payload.get("import_id"),
        "decision": decision,
        "margen": margen
    }