# ============================================================
# ZYRA / NEXO
# ROOT APPLICATION ROUTER — ENTERPRISE 3.0
# Business Layer Aggregator
# Clean • Stable • Production Ready
# ============================================================

from fastapi import APIRouter

# ============================================================
# IMPORT MASTER BUSINESS ROUTER
# ============================================================

from app.Routers.router_router import router as api_router

# ============================================================
# ROOT ROUTER INSTANCE
# ============================================================

router = APIRouter()

# ============================================================
# REGISTER BUSINESS LAYER
# ============================================================

router.include_router(
    api_router,
    prefix="",
    tags=["ZYRA NEXO API"]
)
