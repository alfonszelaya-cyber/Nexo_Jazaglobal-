# ============================================================
# ZYRA / NEXO
# ROOT APPLICATION ROUTER — ENTERPRISE 3.0
# Conecta únicamente la capa de Routers (Business Layer)
# ============================================================

from fastapi import APIRouter

# ============================================================
# IMPORT MASTER ROUTER (Business Layer)
# ============================================================

from app.Routers.router_router import router as api_router

# ============================================================
# ROOT ROUTER
# ============================================================

router = APIRouter()

# ============================================================
# REGISTER BUSINESS ROUTERS
# ============================================================

router.include_router(api_router)
