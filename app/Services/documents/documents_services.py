# ============================================================
# ZYRA / NEXO
# DOCUMENTS SERVICE — ENTERPRISE 3.0
# Document Processing Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class DocumentsServices:
    """
    Enterprise Documents Service

    - Stores and archives documents
    - Emits system events
    - Registers immutable ledger traces
    """

    # ========================================================
    # UPLOAD DOCUMENT
    # ========================================================

    def upload_document(self, owner_id: str, document_type: str) -> Dict[str, Any]:

        result = {
            "document_id": str(uuid.uuid4()),
            "owner_id": owner_id,
            "document_type": document_type,
            "status": "stored",
            "uploaded_at": datetime.utcnow()
        }

        # Emit event to CORE
        route_event(
            event_type="FACTURA_EMITIDA",
            payload=result,
            source="DOCUMENTS_SERVICE"
        )

        # Ledger trace
        ledger_record(
            evento="DOCUMENT_UPLOADED",
            estado="OK",
            payload=result,
            origen="DOCUMENTS_SERVICE"
        )

        return result

    # ========================================================
    # ARCHIVE DOCUMENT
    # ========================================================

    def archive_document(self, document_id: str) -> Dict[str, Any]:

        result = {
            "document_id": document_id,
            "status": "archived",
            "archived_at": datetime.utcnow()
        }

        # Emit archive event
        route_event(
            event_type="ALERTA_ZYRA",
            payload=result,
            source="DOCUMENTS_SERVICE"
        )

        # Ledger trace
        ledger_record(
            evento="DOCUMENT_ARCHIVED",
            estado="OK",
            payload=result,
            origen="DOCUMENTS_SERVICE"
        )

        return result
