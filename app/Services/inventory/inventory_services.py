# ============================================================
# ZYRA / NEXO
# INVENTORY SERVICE — ENTERPRISE 3.0
# Inventory Management Logic Layer
# ============================================================

import uuid
from datetime import datetime
from typing import Dict, Any

# ============================================================
# CORE / INFRA CONNECTIONS
# ============================================================

from Core.inventory_engine import register_product_in_core, update_product_stock_in_core
from Core.core_ledger import ledger_record
from infrastructure.events.event_router import route_event


class InventoryService:
    """
    Enterprise Inventory Service

    - Registers product inside Core inventory engine
    - Updates stock via Core
    - Emits system events
    - Writes immutable ledger trace
    """

    # ========================================================
    # ADD PRODUCT
    # ========================================================

    def add_product(self, name: str, quantity: int) -> Dict[str, Any]:

        if not name:
            raise ValueError("Product name required")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        product_id = str(uuid.uuid4())

        # Register in Core
        register_product_in_core(
            product_id=product_id,
            name=name,
            quantity=quantity
        )

        result = {
            "product_id": product_id,
            "name": name,
            "quantity": quantity,
            "status": "created",
            "created_at": datetime.utcnow()
        }

        # Emit Event
        route_event(
            event_type="PRODUCT_CREATED",
            payload=result,
            source="INVENTORY_SERVICE"
        )

        # Ledger Record
        ledger_record(
            evento="PRODUCT_CREATED",
            estado="SUCCESS",
            payload=result,
            origen="INVENTORY_SERVICE"
        )

        return result

    # ========================================================
    # UPDATE STOCK
    # ========================================================

    def update_stock(self, product_id: str, quantity: int) -> Dict[str, Any]:

        if not product_id:
            raise ValueError("Product ID required")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        # Update in Core
        update_product_stock_in_core(
            product_id=product_id,
            quantity=quantity
        )

        result = {
            "product_id": product_id,
            "new_quantity": quantity,
            "updated_at": datetime.utcnow()
        }

        # Emit Event
        route_event(
            event_type="STOCK_UPDATED",
            payload=result,
            source="INVENTORY_SERVICE"
        )

        # Ledger Record
        ledger_record(
            evento="STOCK_UPDATED",
            estado="SUCCESS",
            payload=result,
            origen="INVENTORY_SERVICE"
        )

        return result
