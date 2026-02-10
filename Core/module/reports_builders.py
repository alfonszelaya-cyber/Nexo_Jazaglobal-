# ============================================================
# reports_builders.py
# NEXO / ZYRA — REPORTES & BI
# CONSTRUCTORES DE REPORTES
# PASIVO | SIN AUTOEJECUCIÓN
# ============================================================

def build_report(report_meta: dict, data: list) -> dict:
    """
    Construye el cuerpo final de un reporte.
    """
    return {
        "report_id": report_meta.get("report_id"),
        "type": report_meta.get("type"),
        "period": report_meta.get("period"),
        "filters": report_meta.get("filters", {}),
        "rows": data,
        "totals": {
            "count": len(data)
        }
    }