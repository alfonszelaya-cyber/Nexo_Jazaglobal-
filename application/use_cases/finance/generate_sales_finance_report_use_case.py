# ============================================================
# ZYRA / NEXO
# GENERATE SALES FINANCE REPORT USE CASE
# Enterprise 3.0 – Clean Architecture
# ============================================================

from Core.module.template.template_registry import get_template


class GenerateSalesFinanceReportUseCase:

    def __init__(self):
        self.template_name = "SALES_FINANCE_REPORT"

    def execute(self, payload: dict) -> dict:
        """
        Genera un reporte financiero de ventas basado en plantilla oficial.
        """

        # 1️⃣ Obtener plantilla oficial
        template = get_template(self.template_name)

        # 2️⃣ Clonar estructura base
        report = template.copy()

        # 3️⃣ Inyectar datos del payload si existen
        if "company_profile" in payload:
            report["company_profile"].update(payload["company_profile"])

        if "sales_metrics" in payload:
            report["sales_metrics"].update(payload["sales_metrics"])

        if "reporting_period" in payload:
            report["reporting_period"].update(payload["reporting_period"])

        # 4️⃣ Marcar como generado
        report["report_metadata"]["status"] = "FINAL"

        return report
