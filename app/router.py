# ============================================================
# ZYRA / NEXO
# ROOT APPLICATION ROUTER — ENTERPRISE 3.0
# Business Layer Aggregator
# Clean • Stable • Production Ready
# ============================================================

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# ============================================================
# DATABASE & MODELS
# ============================================================

from app.database import get_db
from app.models.user_model import User

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

# ============================================================
# DATABASE TEST ENDPOINT
# ============================================================

@router.get("/users", tags=["Database Test"])
def list_users(db: Session = Depends(get_db)):
    """
    Returns all users from PostgreSQL.
    """
    users = db.query(User).all()
    return users
