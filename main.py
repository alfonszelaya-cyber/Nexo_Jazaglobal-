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
# CONFIGURACIÓN BASE
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

app = FastAPI(
    title="ZYRA NEXO CORE",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# ============================================================
# INCLUIR ROUTER PRINCIPAL
# ============================================================

from app.router import router as api_router
app.include_router(api_router)

# ============================================================
# LOADER DINÁMICO TOTAL
# ============================================================

EXCLUDED_FOLDERS = {
    "__pycache__",
    ".venv",
    "venv",
    ".git",
    ".idea",
    ".pytest_cache"
}

def load_system_modules():
    loaded = []
    errors = []

    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]

        for file in files:
            if file.endswith(".py") and not file.startswith("__"):

                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, BASE_DIR)
                module_name = rel_path.replace(os.sep, ".").replace(".py", "")

                try:
                    importlib.import_module(module_name)
                    loaded.append(module_name)
                except Exception as e:
                    errors.append({module_name: str(e)})

    return {
        "total_loaded": len(loaded),
        "total_errors": len(errors),
        "loaded": loaded,
        "errors": errors
    }

# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "system": "ZYRA_NEXO_CORE",
        "version": "3.0.0",
        "status": "running"
    }

# ============================================================
# BOOT
# ============================================================

@app.get("/core/boot")
def boot_system():
    return load_system_modules()
