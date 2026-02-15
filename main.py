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

# Como tú dijiste: Main levanta App, y App levanta el resto a través del Router
from app.router import router as api_router
app.include_router(api_router)

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

    # Escaneo profundo para verificar la salud de todos los archivos .py
    for root, dirs, files in os.walk(BASE_DIR):

        # Excluir carpetas que no son código
        dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]

        for file in files:
            # Solo archivos Python que no sean el main ni inits
            if file.endswith(".py") and not file.startswith("__") and file != "main.py":

                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, BASE_DIR)

                # Convertir ruta de archivo a nombre de módulo (app.Services.ai.ai_services)
                module_name = rel_path.replace(os.sep, ".").replace(".py", "")

                try:
                    # Intenta importar el módulo para ver si tiene errores de sintaxis o rutas
                    importlib.import_module(module_name)
                    loaded.append(module_name)
                except Exception as e:
                    # Aquí es donde capturamos el error de "Cannot import name AIServices"
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
    # Este endpoint activa la lectura que me mostraste en las fotos
    return load_system_modules()
