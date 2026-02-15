# ============================================================
# ZYRA / NEXO
# MASTER SCHEMA REGISTRY — ENTERPRISE 3.0
# Schemas Layer Aggregator
# File: app/Schemas/router_schema.py
# ============================================================

from fastapi import APIRouter

# ============================================================
# IMPORT ALL SCHEMA MODULES
# (IMPORTANT: Folder name must be "Schemas" with capital S)
# ============================================================

from app.Schemas.ai.ai_schema import router as ai_schema
from app.Schemas.analytics.analytics_schema import router as analytics_schema
from app.Schemas.audit.audit_schema import router as audit_schema
from app.Schemas.auth.auth_schema import router as auth_schema
from app.Schemas.billing.billing_schema import router as billing_schema
from app.Schemas.compliance.compliance_schema import router as compliance_schema
from app.Schemas.contracts.contracts_schema import router as contracts_schema
from app.Schemas.documents.documents_schema import router as documents_schema
from app.Schemas.finance.finance_schema import router as finance_schema
from app.Schemas.integrations.integrations_schema import router as integrations_schema
from app.Schemas.inventory.inventory_schema import router as inventory_schema
from app.Schemas.logistics.logistics_schema import router as logistics_schema
from app.Schemas.notifications.notifications_schema import router as notifications_schema
from app.Schemas.operations.operations_schema import router as operations_schema
from app.Schemas.payments.payments_schema import router as payments_schema
from app.Schemas.reports.reports_schema import router as reports_schema
from app.Schemas.roles.roles_schema import router as roles_schema
from app.Schemas.security.security_schema import router as security_schema
from app.Schemas.system.system_schema import router as system_schema
from app.Schemas.users.users_schema import router as users_schema


# ============================================================
# MASTER SCHEMA ROUTER (NO PREFIX)
# ============================================================

router = APIRouter()


# ============================================================
# REGISTER ALL SCHEMAS
# ============================================================

router.include_router(ai_schema)
router.include_router(analytics_schema)
router.include_router(audit_schema)
router.include_router(auth_schema)
router.include_router(billing_schema)
router.include_router(compliance_schema)
router.include_router(contracts_schema)
router.include_router(documents_schema)
router.include_router(finance_schema)
router.include_router(integrations_schema)
router.include_router(inventory_schema)
router.include_router(logistics_schema)
router.include_router(notifications_schema)
router.include_router(operations_schema)
router.include_router(payments_schema)
router.include_router(reports_schema)
router.include_router(roles_schema)
router.include_router(security_schema)
router.include_router(system_schema)
router.include_router(users_schema)
