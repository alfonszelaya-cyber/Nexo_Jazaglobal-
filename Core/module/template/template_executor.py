# ============================================================
# ZYRA / NEXO
# TEMPLATE EXECUTOR CANÓNICO
# Ejecuta flujos basados en plantillas registradas
# 10+ AÑOS – CORE SAFE
# ============================================================

import copy
from datetime import datetime, timezone

from template_registry import get_template
from event_router import route_event

# =========================
# UTILIDADES
# =========================

def _now():
    return datetime.now(timezone.utc).isoformat()


def activate_template(template_name: str, data: dict, event_type: str, source="TEMPLATE_EXECUTOR"):
    """
    Activa una plantilla:
    - Clona la plantilla base
    - Inyecta datos
    - Sella timestamps
    - Envía evento al CORE
    """

    base_template = get_template(template_name)
    instance = copy.deepcopy(base_template)

    # -------------------------
    # Inyectar metadata básica
    # -------------------------
    if "flow_metadata" in instance:
        instance["flow_metadata"]["flow_id"] = data.get("flow_id", "AUTO")
        instance["flow_metadata"]["created_at"] = _now()
        instance["flow_metadata"]["status"] = data.get("status", instance["flow_metadata"].get("status"))

    if "report_metadata" in instance:
        instance["report_metadata"]["report_id"] = data.get("report_id", "AUTO")
        instance["report_metadata"]["created_at"] = _now()
        instance["report_metadata"]["status"] = data.get("status", instance["report_metadata"].get("status"))

    # -------------------------
    # Inyectar datos del usuario
    # -------------------------
    for key, value in data.items():
        if key in instance:
            instance[key] = value

    # -------------------------
    # Emitir evento al CORE
    # -------------------------
    result = route_event(
        event_type=event_type,
        payload=instance,
        source=source
    )

    return {
        "template": template_name,
        "event": event_type,
        "status": "ACTIVATED",
        "timestamp": _now(),
        "core_result": result,
        "instance": instance
    }

# =========================
# API ESPECÍFICA POR FLUJO
# =========================

def run_sales_flow(data: dict):
    return activate_template("SALES_FLOW", data, "VENTA")

def run_import_export_flow(data: dict):
    return activate_template("IMPORT_EXPORT_FLOW", data, "IMPORTACION")

def run_payment_flow(data: dict):
    return activate_template("PAYMENT_FLOW", data, "PAGO")

def run_payroll_flow(data: dict):
    return activate_template("PAYROLL_FLOW", data, "PAGO")

def run_business_flow(data: dict):
    return activate_template("BUSINESS_FLOW", data, "NEGOCIO")

def run_fiscal_document(data: dict):
    return activate_template("FISCAL_DOCUMENT", data, "FACTURA_EMITIDA")

def run_financial_report(data: dict):
    return activate_template("FINANCIAL_REPORT", data, "REPORTE_FINANCIERO")

# ============================================================
# REGLAS
# - NO imprime
# - NO guarda
# - NO valida contenido
# - SOLO activa flujos
# - CORE decide consecuencias
# ============================================================