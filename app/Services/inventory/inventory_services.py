# ============================================================
# ZYRA / NEXO
# INVENTORY SERVICE — ENTERPRISE 3.0
# Inventory Management Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict


class InventoryService:

    @staticmethod
    def add_product(name: str, quantity: int) -> Dict:

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        return {
            "product_id": str(uuid.uuid4()),
            "name": name,
            "quantity": quantity,
            "status": "created",
            "created_at": datetime.utcnow()
        }

    @staticmethod
    def update_stock(product_id: str, quantity: int) -> Dict:

        return {
            "product_id": product_id,
            "new_quantity": quantity,
            "updated_at": datetime.utcnow()
        }
