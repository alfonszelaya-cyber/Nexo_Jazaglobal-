# ============================================================
# ZYRA / NEXO
# GENERATE SALES FINANCE REPORT USE CASE
# Enterprise 3.0 – Clean Architecture
# ============================================================

from copy import deepcopy
from Core.module.template.template_registry import get_template


class GenerateSalesFinanceReportUseCase:
    """
    Use Case oficial para generar reporte financiero de ventas.
    - No accede a base de datos
    - No imprime
    - No muta plantilla original
    - Usa registry oficial
    """

    def __init__(self):
        self.template_name = "SALES_FINANCE_REPORT"

    def execute(self, payload: dict) -> dict:
        if not isinstance(payload, dict):
            raise ValueError("Payload inválido. Debe ser un diccionario.")

        # 1️⃣ Obtener plantilla oficial desde registry
        template = get_template(self.template_name)

        # 2️⃣ Clonar profundo (evita modificar la plantilla base)
        report = deepcopy(template)

        # 3️⃣ Inyectar datos permitidos
        report["company_profile"].update(payload.get("company_profile", {}))
        report["sales_metrics"].update(payload.get("sales_metrics", {}))
        report["reporting_period"].update(payload.get("reporting_period", {}))

        # 4️⃣ Actualizar estado
        report["report_metadata"]["status"] = "FINAL"

        return report
