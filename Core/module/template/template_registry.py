# ============================================================
# ZYRA / NEXO
# TEMPLATE REGISTRY CANÓNICO (RUNNER UNIVERSAL DE PLANTILLAS)
# ENTERPRISE 3.0 – CORE SAFE – INMUTABLE
# ============================================================

"""
Este archivo:

- NO ejecuta lógica de negocio
- NO imprime
- NO guarda datos
- SOLO registra y expone plantillas oficiales
- Es el punto único para que el CORE cargue plantillas
"""

# =========================
# IMPORTAR TODAS LAS PLANTILLAS
# =========================

from Core.module.template.sales_flow_template import SALES_FLOW_TEMPLATE
from Core.module.template.sales_payment_flow_template import SALES_PAYMENT_FLOW_TEMPLATE
from Core.module.template.import_export_flow_template import IMPORT_EXPORT_FLOW_TEMPLATE
from Core.module.template.payment_flow_template import PAYMENT_FLOW_TEMPLATE
from Core.module.template.payroll_payment_flow_template import PAYROLL_PAYMENT_FLOW_TEMPLATE
from Core.module.template.business_flow_template import BUSINESS_FLOW_TEMPLATE

# ⚠️ ESTA ES LA ÚNICA VARIABLE EN MINÚSCULA
from Core.module.template.financial_report_template import financial_report_template

from Core.module.template.sales_finances_report_template import SALES_FINANCE_REPORT_TEMPLATE
from Core.module.template.fiscal_document_template import FISCAL_DOCUMENT_TEMPLATE
from Core.module.template.fiscal_country_template import FISCAL_COUNTRY_TEMPLATE
from Core.module.template.global_currency_conversion_template import GLOBAL_CURRENCY_CONVERSION_TEMPLATE


# =========================
# REGISTRO MAESTRO
# =========================

TEMPLATE_REGISTRY = {

    # --- FLOWS ---
    "SALES_FLOW": SALES_FLOW_TEMPLATE,
    "SALES_PAYMENT_FLOW": SALES_PAYMENT_FLOW_TEMPLATE,
    "IMPORT_EXPORT_FLOW": IMPORT_EXPORT_FLOW_TEMPLATE,
    "PAYMENT_FLOW": PAYMENT_FLOW_TEMPLATE,
    "PAYROLL_FLOW": PAYROLL_PAYMENT_FLOW_TEMPLATE,
    "BUSINESS_FLOW": BUSINESS_FLOW_TEMPLATE,

    # --- DOCUMENTOS ---
    "FISCAL_DOCUMENT": FISCAL_DOCUMENT_TEMPLATE,
    "FISCAL_COUNTRY": FISCAL_COUNTRY_TEMPLATE,

    # --- REPORTES ---
    "FINANCIAL_REPORT": financial_report_template,
    "SALES_FINANCE_REPORT": SALES_FINANCE_REPORT_TEMPLATE,

    # --- MONEDA ---
    "CURRENCY_CONVERSION": GLOBAL_CURRENCY_CONVERSION_TEMPLATE,
}


# =========================
# API CANÓNICA
# =========================

def get_template(template_name: str) -> dict:
    name = template_name.strip().upper()
    if name not in TEMPLATE_REGISTRY:
        raise ValueError(f"Plantilla no registrada: {name}")
    return TEMPLATE_REGISTRY[name]


def list_templates() -> list:
    return sorted(TEMPLATE_REGISTRY.keys())


def template_exists(template_name: str) -> bool:
    return template_name.strip().upper() in TEMPLATE_REGISTRY
