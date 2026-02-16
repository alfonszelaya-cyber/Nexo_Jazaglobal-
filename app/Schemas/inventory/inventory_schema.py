# ============================================================
# ZYRA / NEXO
# INVENTORY SCHEMA — ENTERPRISE 3.0
# Inventory & Stock Control Layer
# File: app/Schemas/inventory/inventory_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class InventoryStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# CREATE PRODUCT
# ============================================================

class ProductCreateRequest(BaseModel):
    sku: str
    name: str
    category: Optional[str] = None
    quantity: int = Field(..., ge=0)
    unit_price: float = Field(..., ge=0)
    currency: str


class ProductCreateResponse(BaseModel):
    product_id: str
    sku: str
    name: str
    category: Optional[str] = None
    quantity: int
    unit_price: float
    currency: str
    status: str
    created_at: datetime


# ============================================================
# STOCK UPDATE
# ============================================================

class StockUpdateRequest(BaseModel):
    product_id: str
    quantity_change: int
    reason: Optional[str] = None


class StockUpdateResponse(BaseModel):
    movement_id: str
    product_id: str
    quantity_change: int
    resulting_stock: int
    timestamp: datetime


# ============================================================
# STOCK CHECK
# ============================================================

class StockCheckRequest(BaseModel):
    product_id: str


class StockCheckResponse(BaseModel):
    product_id: str
    available_stock: int
    checked_at: datetime
