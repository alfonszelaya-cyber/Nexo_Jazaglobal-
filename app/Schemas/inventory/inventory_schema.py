# ============================================================
# ZYRA / NEXO
# INVENTORY SCHEMA — ENTERPRISE 3.0
# Inventory & Stock Control Layer
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# CREATE PRODUCT
# ============================================================

class CreateProductRequest(BaseModel):
    sku: str
    name: str
    category: Optional[str]
    quantity: int = Field(..., ge=0)
    unit_price: float = Field(..., ge=0)
    currency: str


class ProductResponse(BaseModel):
    product_id: str
    sku: str
    name: str
    quantity: int
    unit_price: float
    currency: str
    status: str  # ACTIVE | INACTIVE
    created_at: datetime


# ============================================================
# STOCK UPDATE
# ============================================================

class UpdateStockRequest(BaseModel):
    product_id: str
    quantity_change: int  # puede ser negativo
    reason: Optional[str]


class StockMovementResponse(BaseModel):
    movement_id: str
    product_id: str
    quantity_change: int
    resulting_stock: int
    timestamp: datetime
