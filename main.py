from fastapi import FastAPI
from core.health_check import run_health_check

# Importaciones reales del CORE
from core.accounting_engine import *
from core.audit_engine import *
from core.inventory_engine import *
from core.bunker_engine import *

app = FastAPI(title="ZYRA NEXO CORE")

# =============================
# ROOT
# =============================
@app.get("/")
def root():
    return {
        "system": "ZYRA_NEXO_CORE",
        "status": "running"
    }

# =============================
# HEALTH REAL
# =============================
@app.get("/core/health")
def health():
    return run_health_check()

# =============================
# ACCOUNTING ENGINE
# =============================
@app.get("/engine/accounting")
def accounting_status():
    return {
        "engine": "accounting_engine",
        "status": "connected"
    }

# =============================
# AUDIT ENGINE
# =============================
@app.get("/engine/audit")
def audit_status():
    return {
        "engine": "audit_engine",
        "status": "connected"
    }

# =============================
# INVENTORY ENGINE
# =============================
@app.get("/engine/inventory")
def inventory_status():
    return {
        "engine": "inventory_engine",
        "status": "connected"
    }

# =============================
# BUNKER ENGINE
# =============================
@app.get("/engine/bunker")
def bunker_status():
    return {
        "engine": "bunker_engine",
        "status": "connected"
    }
