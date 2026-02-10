from fastapi import FastAPI
from core.health_check import run_health_check

# Importamos motores reales
from core.inventory_engine import inventario_completo
from core.audit_engine import auditar_declaracion
from core.bunker_engine import register_identity

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
# BUNKER ENGINE REAL
# -----------------------
@app.get("/engine/bunker")
def bunker():
    return {
        "message": "Bunker engine activo",
        "hint": "Use POST para crear identidades"
    }
