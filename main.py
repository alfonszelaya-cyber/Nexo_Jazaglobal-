# ============================================================
# ZYRA / NEXO
# MAIN ENTRYPOINT — ENTERPRISE 3.0
# Clean Bootstrap | Production Ready | Scalable
# ============================================================

from fastapi import FastAPI
import os
import sys
import importlib
from contextlib import asynccontextmanager

# ============================================================
# CONFIGURACIÓN DE RUTAS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ============================================================
# DATABASE IMPORTS
# ============================================================

from app.database import engine, Base
import app.models.user_model  # IMPORTANTE: registra el modelo

# ============================================================
# LIFESPAN (Startup / Shutdown Profesional)
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    print("✅ DATABASE CONNECTED & TABLES READY")
    yield
    # Shutdown
    print("✅ SISTEMA CERRADO CORRECTAMENTE")

# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI(
    title="ZYRA NEXO CORE",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan
)

# ============================================================
# INCLUIR ROUTERS
# ============================================================

# Router principal
from app.router import router
app.include_router(router)

# 🔥 NUEVO — AUTH ROUTER INYECTADO
from app.Routers.auth.auth_router import router as auth_router
app.include_router(auth_router)

# ============================================================
# MOTOR DE ESCANEO DINÁMICO
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
