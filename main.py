from fastapi import FastAPI
from Core.health_check import run_health_check

# Motores reales
from Core.inventory_engine import inventario_completo
from Core.audit_engine import auditar_declaracion
from Core.bunker_engine import register_identity
from Core.accounting_engine import accounting_engine_status  # <-- asegúrate que exista esta función

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
# ACCOUNTING ENGINE REAL
# -----------------------
@app.get("/engine/accounting")
def accounting():
    return accounting_engine_status()

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
    return register_identity(
        full_name="Test User",
        role_name="CLIENT",
        created_by_id="SYSTEM"
    )
