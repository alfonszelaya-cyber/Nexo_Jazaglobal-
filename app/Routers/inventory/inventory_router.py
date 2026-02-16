# ============================================================
# ZYRA / NEXO
# INVENTORY ROUTER — ENTERPRISE 3.0
# Stock Management & Product Control
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.inventory.inventory_schema import (
    InventoryStatusResponse,
    ProductCreateRequest,
    ProductCreateResponse,
    StockUpdateRequest,
    StockUpdateResponse,
    StockCheckRequest,
    StockCheckResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.inventory.inventory_services import InventoryService


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

inventory_service = InventoryService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=InventoryStatusResponse)
def inventory_status():
    return InventoryStatusResponse(
        module="ZYRA_INVENTORY_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# ADD PRODUCT
# ============================================================

@router.post("/add-product", response_model=ProductCreateResponse)
def add_product(payload: ProductCreateRequest):
    try:
        return inventory_service.add_product(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# UPDATE STOCK
# ============================================================

@router.post("/update-stock", response_model=StockUpdateResponse)
def update_stock(payload: StockUpdateRequest):
    return inventory_service.update_stock(payload)


# ============================================================
# CHECK STOCK
# ============================================================

@router.post("/check-stock", response_model=StockCheckResponse)
def check_stock(payload: StockCheckRequest):
    return inventory_service.check_stock(payload)
