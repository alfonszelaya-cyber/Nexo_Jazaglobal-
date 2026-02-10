from fastapi import FastAPI
from Core.health_check import run_health_check

# Importamos motores reales
from Core.inventory_engine import inventario_completo
from Core.audit_engine import auditar_declaracion
from Core.bunker_engine import register_identity

app = FastAPI(title="ZYRA NEXO CORE")

# -----------------------
# ROOT
# -----------------------
@app.get("/")
def root():
    return {
        "system": "ZYRA_NEXO_CORE",
        "status": "running"
    }

# -----------------------
# HEALTH CHECK
# -----------------------
@app.get("/core/health")
def health():
    return run_health_check()

# -----------------------
# INVENTORY ENGINE REAL
# -----------------------
@app.get("/engine/inventory")
def inventory():
    return inventario_completo()

# -----------------------
# AUDIT ENGINE REAL
# -----------------------
@app.get("/engine/audit")
def audit():
    return auditar_declaracion()

# -----------------------
# BUNKER ENGINE
# -----------------------
@app.get("/engine/bunker")
def bunker():
    return {
        "engine": "bunker_engine",
        "status": "active"
    }
