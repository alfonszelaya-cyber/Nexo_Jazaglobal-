# audit_reports.py
# NEXO / ZYRA — AUDITORÍA & TRAZABILIDAD
# REPORTES DE AUDITORÍA
# PASIVO

def generate_audit_report(trail: list) -> dict:
    """
    Genera un resumen básico de auditoría.
    """
    return {
        "total_records": len(trail),
        "actors": list({r.get("actor") for r in trail}),
        "actions": list({r.get("action") for r in trail})
    }