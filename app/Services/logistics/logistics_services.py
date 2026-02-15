# ============================================================
# ZYRA / NEXO
# LOGISTICS SERVICE — ENTERPRISE 3.0
# Logistics & Shipment Management Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict


class LogisticsService:

    @staticmethod
    def create_shipment(origin: str, destination: str) -> Dict:

        return {
            "shipment_id": str(uuid.uuid4()),
            "origin": origin,
            "destination": destination,
            "status": "in_transit",
            "created_at": datetime.utcnow()
        }

    @staticmethod
    def confirm_delivery(shipment_id: str) -> Dict:

        return {
            "shipment_id": shipment_id,
            "status": "delivered",
            "delivered_at": datetime.utcnow()
        }
