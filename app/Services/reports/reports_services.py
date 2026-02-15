
# ============================================================
# ZYRA / NEXO
# REPORTS SERVICE — ENTERPRISE 3.0
# Reporting & Aggregation Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / TEMPLATE / INFRA CONNECTIONS
# ============================================================

from Core.module.reports_engine import build_report
from Core.module.template.template_runner import run_template
from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class ReportsService:
    """
    Enterprise Reports Service

    - Builds reports using Core logic
    - Executes reporting templates
    - Emits system events
    - Writes immutable ledger trace
    """

    # ========================================================
    # GENERATE REPORT
    # ========================================================

    def generate_report(self, report_type: str, filters: Dict[str, Any]) -> Dict[str, Any]:

        if not report_type:
            raise ValueError("Report type required")

        report_id = str(uuid.uuid4())

        # Execute Core reporting logic
        core_data = build_report(report_type, filters)

        # Run template layer
        formatted_output = run_template(
            template_name="financial_report_template",
            payload=core_data
        )

        result = {
            "report_id": report_id,
            "type": report_type,
            "filters": filters,
            "status": "generated",
            "data": formatted_output,
            "generated_at": datetime.utcnow()
        }

        # Emit system event
        route_event(
            event_type="REPORT_GENERATED",
            payload=result,
            source="REPORTS_SERVICE"
        )

        # Ledger trace
        ledger_record(
            evento="REPORT_GENERATED",
            estado="SUCCESS",
            payload={"report_id": report_id, "type": report_type},
            origen="REPORTS_SERVICE"
        )

        return result

    # ========================================================
    # GET REPORT
    # ========================================================

    def get_report(self, report_id: str) -> Dict[str, Any]:

        if not report_id:
            raise ValueError("Report ID required")

        result = {
            "report_id": report_id,
            "status": "ready",
            "retrieved_at": datetime.utcnow()
        }

        ledger_record(
            evento="REPORT_RETRIEVED",
            estado="INFO",
            payload={"report_id": report_id},
            origen="REPORTS_SERVICE"
        )

        return result
