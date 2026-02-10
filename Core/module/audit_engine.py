# audit_engine.py
# NEXO / ZYRA — AUDITORÍA & TRAZABILIDAD
# MOTOR CENTRAL DE AUDITORÍA
# PASIVO | SOLO REGISTRA

from datetime import datetime, timezone

def record_audit(entry: dict) -> dict:
    """
    Registra una entrada de auditoría (sin persistir).
    La persistencia la maneja el listener del módulo.
    """
    return {
        "audit_id": entry.get("audit_id"),
        "actor": entry.get("actor"),
        "action": entry.get("action"),
        "entity": entry.get("entity"),
        "details": entry.get("details", {}),
        "ts": datetime.now(timezone.utc).isoformat()
    }