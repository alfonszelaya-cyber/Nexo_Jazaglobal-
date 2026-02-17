# ============================================================
# ZYRA / NEXO
# MAIN ENTRYPOINT — ENTERPRISE 3.0
# Clean Bootstrap | Production Ready | Scalable
# ============================================================

from fastapi import FastAPI
import os
import sys
import importlib

# ============================================================
# CONFIGURACIÓN DE RUTAS (CRÍTICO PARA LOS 18 ERRORES)
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Esto permite que el Router de la App y los Servicios se encuentren entre sí
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

app = FastAPI(
    title="ZYRA NEXO CORE",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# ============================================================
# INCLUIR ROUTER PRINCIPAL (EL QUE CONSUME LOS SERVICIOS)
# ============================================================

from app.router import router as api_router
app.include_router(api_router)

# ============================================================
# 🔥 INYECCIÓN ENTERPRISE — DATABASE INIT
# (NO rompe nada existente)
# ============================================================

try:
    from infrastructure.database.db_init import init_db

    @app.on_event("startup")
    async def startup_event():
        init_db()
        print("✅ DATABASE CONNECTED")

except Exception as e:
    print("⚠️ Database init skipped:", str(e))

# ============================================================
# MOTOR DE LECTURA Y ESCANEO DINÁMICO
# ============================================================

EXCLUDED_FOLDERS = {
    "__pycache__",
    ".venv",
    "venv",
    ".git",
    ".idea",
    ".pytest_cache",
    "data"
}

def load_system_modules():
    loaded = []
    errors = []

    for root, dirs, files in os.walk(BASE_DIR):

        dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]

        for file in files:
            if file.endswith(".py") and not file.startswith("__") and file != "main.py":

                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, BASE_DIR)

                module_name = rel_path.replace(os.sep, ".").replace(".py", "")

                try:
                    importlib.import_module(module_name)
                    loaded.append(module_name)
                except Exception as e:
                    errors.append({
                        "module": module_name,
                        "error": str(e)
                    })

    return {
        "status": "BOOT_SCAN_COMPLETED",
        "total_loaded": len(loaded),
        "total_errors": len(errors),
        "errors": errors
    }

# ============================================================
# ENDPOINTS DE CONTROL
# ============================================================

@app.get("/")
def root():
    return {
        "system": "ZYRA_NEXO_CORE",
        "version": "3.0.0",
        "status": "running",
        "environment": "PRODUCTION"
    }

@app.get("/core/boot")
def boot_system():
    return load_system_modules()
