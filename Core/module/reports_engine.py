# ============================================================
# reports_engine.py
# NEXO / ZYRA — REPORTES & BI
# MOTOR DE REPORTES
# PASIVO | EVENT-DRIVEN | ENTERPRISE READY
# ============================================================

from datetime import datetime, timezone
import uuid

# ============================================================
# UTILIDAD TIEMPO
# ============================================================

def _now():
    return datetime.now(timezone.utc).isoformat()


# ============================================================
# GENERAR REPORTE BASE
# ============================================================

def generate_report(payload: dict) -> dict:
    """
    Genera un reporte base (sin persistir).
    """

    report_id = payload.get("report_id") or str(uuid.uuid4())

    return {
        "report_id": report_id,
        "type": payload.get("type"),
        "period": payload.get("period"),
        "filters": payload.get("filters", {}),
        "generated_by": payload.get("generated_by"),
        "status": "GENERATED",
        "created_at": _now()
    }


# ============================================================
# BUILD REPORT (COMPATIBLE CON ROUTERS)
# ============================================================

def build_report(
    report_type: str,
    start_date: str = None,
    end_date: str = None,
    filters: dict = None,
    generated_by: str = None
) -> dict:

    report_id = str(uuid.uuid4())

    return {
        "report_id": report_id,
        "report_type": report_type,
        "start_date": start_date,
        "end_date": end_date,
        "filters": filters or {},
        "generated_by": generated_by,
        "status": "GENERATED",
        "generated_at": _now()
    }


# ============================================================
# GET REPORT
# ============================================================

def get_report_in_core(report_id: str) -> dict:
    return {
        "report_id": report_id,
        "status": "READY",
        "retrieved_at": _now()
    }


# ============================================================
# LIST REPORTS
# ============================================================

def list_reports_in_core() -> dict:
    return {
        "total_reports": 0,
        "reports": [],
        "listed_at": _now()
    }


# ============================================================
# CANCEL REPORT
# ============================================================

def cancel_report_in_core(report_id: str) -> dict:
    return {
        "report_id": report_id,
        "status": "CANCELLED",
        "cancelled_at": _now()
    }
