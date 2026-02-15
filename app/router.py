# ============================================================
# ZYRA / NEXO
# ROOT APPLICATION ROUTER — ENTERPRISE 3.0
# Conecta Routers + Schemas Layer
# ============================================================

from fastapi import APIRouter

# ============================================================
# IMPORT MASTER ROUTERS
# ============================================================

from app.Routers.router_router import router as api_router
from app.Schemas.router_schema import router as schema_router

# ============================================================
# ROOT ROUTER
# ============================================================

router = APIRouter()

# ============================================================
# REGISTER LAYERS
# ============================================================

# API Business Layer
router.include_router(api_router)

# Schemas Introspection Layer (opcional para debug)
router.include_router(schema_router)
