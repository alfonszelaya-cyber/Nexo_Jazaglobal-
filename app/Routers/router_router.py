# ============================================================
# ZYRA / NEXO
# MASTER ROUTER REGISTRY — ENTERPRISE 3.0
# Routers Layer Aggregator
# File: app/Routers/router_router.py
# ============================================================

from fastapi import APIRouter

# ============================================================
# IMPORT ALL MODULE ROUTERS
# (IMPORTANT: Folder name must be "Routers" with capital R)
# ============================================================

from app.Routers.ai.ai_router import router as ai_router
from app.Routers.audit.audit_router import router as audit_router
from app.Routers.auth.auth_router import router as auth_router
from app.Routers.billing.billing_router import router as billing_router
from app.Routers.compliance.compliance_router import router as compliance_router
from app.Routers.contracts.contracts_router import router as contracts_router
from app.Routers.documents.documents_router import router as documents_router
from app.Routers.finance.finance_router import router as finance_router
from app.Routers.integrations.integrations_router import router as integrations_router
from app.Routers.inventory.inventory_router import router as inventory_router
from app.Routers.logistics.logistics_router import router as logistics_router
from app.Routers.notifications.notifications_router import router as notifications_router
from app.Routers.operations.operations_router import router as operations_router
from app.Routers.payments.payments_router import router as payments_router
from app.Routers.reports.reports_router import router as reports_router
from app.Routers.roles.roles_router import router as roles_router
from app.Routers.security.security_router import router as security_router
from app.Routers.system.system_router import router as system_router
from app.Routers.users.users_router import router as users_router


# ============================================================
# MASTER ROUTER (NO PREFIX HERE)
# The global prefix must be defined in app/router.py
# ============================================================

router = APIRouter()


# ============================================================
# REGISTER ALL MODULE ROUTERS
# ============================================================

router.include_router(ai_router)
router.include_router(audit_router)
router.include_router(auth_router)
router.include_router(billing_router)
router.include_router(compliance_router)
router.include_router(contracts_router)
router.include_router(documents_router)
router.include_router(finance_router)
router.include_router(integrations_router)
router.include_router(inventory_router)
router.include_router(logistics_router)
router.include_router(notifications_router)
router.include_router(operations_router)
router.include_router(payments_router)
router.include_router(reports_router)
router.include_router(roles_router)
router.include_router(security_router)
router.include_router(system_router)
router.include_router(users_router)
