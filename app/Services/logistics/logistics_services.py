# ============================================================
# ZYRA / NEXO
# LOGISTICS SERVICE — ENTERPRISE 3.0
# Logistics & Shipment Management Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.module.shipment_engine import register_shipment_in_core, confirm_delivery_in_core
from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class LogisticsService:
    """
    Enterprise Logistics Service

    - Registers shipment inside Core logistics engine
    - Confirms delivery via Core
    - Emits system events
    - Writes immutable ledger trace
    """

    # ========================================================
    # CREATE SHIPMENT
    # ========================================================

    def create_shipment(self, origin: str, destination: str) -> Dict[str, Any]:

        if not origin or not destination:
            raise ValueError("Origin and destination are required")

        shipment_id = str(uuid.uuid4())

        # Register in Core
        register_shipment_in_core(
            shipment_id=shipment_id,
            origin=origin,
            destination=destination
        )

        result = {
            "shipment_id": shipment_id,
            "origin": origin,
            "destination": destination,
            "status": "in_transit",
            "created_at": datetime.utcnow()
        }

        # Emit Event
        route_event(
            event_type="SHIPMENT_CREATED",
            payload=result,
            source="LOGISTICS_SERVICE"
        )

        # Ledger Record
        ledger_record(
            evento="SHIPMENT_CREATED",
            estado="SUCCESS",
            payload=result,
            origen="LOGISTICS_SERVICE"
        )

        return result

    # ========================================================
    # CONFIRM DELIVERY
    # ========================================================

    def confirm_delivery(self, shipment_id: str) -> Dict[str, Any]:

        if not shipment_id:
            raise ValueError("Shipment ID required")

        # Confirm in Core
        confirm_delivery_in_core(shipment_id)

        result = {
            "shipment_id": shipment_id,
            "status": "delivered",
            "delivered_at": datetime.utcnow()
        }

        # Emit Event
        route_event(
            event_type="SHIPMENT_DELIVERED",
            payload=result,
            source="LOGISTICS_SERVICE"
        )

        # Ledger Record
        ledger_record(
            evento="SHIPMENT_DELIVERED",
            estado="SUCCESS",
            payload=result,
            origen="LOGISTICS_SERVICE"
        )

        return result
