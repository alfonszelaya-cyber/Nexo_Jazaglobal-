from fastapi import FastAPI
from Core.health_check import run_health_check
import Core.inventory_engine as inventory_engine
import Core.audit_engine as audit_engine
import Core.bunker_engine as bunker_engine
import Core.accounting_engine as accounting_engine

app = FastAPI(title="ZYRA NEXO CORE")

@app.get("/")
def root():
    return {
        "system": "ZYRA_NEXO_CORE",
        "status": "running"
    }

@app.get("/core/health")
def health():
    return run_health_check()

@app.get("/engine/inventory")
def inventory():
    return {"engine": "inventory_engine", "status": "active"}

@app.get("/engine/audit")
def audit():
    return {"engine": "audit_engine", "status": "active"}

@app.get("/engine/bunker")
def bunker():
    return {"engine": "bunker_engine", "status": "active"}

@app.get("/engine/accounting")
def accounting():
    return {"engine": "accounting_engine", "status": "active"}
