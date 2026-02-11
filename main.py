from fastapi import FastAPI
import os
import sys
import importlib

# ==============================
# CONFIGURACIÓN BASE SEGURA
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ÚNICO AGREGADO: Esto hace que Python vea tus carpetas y no dé error de "No module named"
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

app = FastAPI(title="ZYRA NEXO CORE")

# ==============================
# CONFIGURACIÓN DE EXCLUSIONES
# ==============================

EXCLUDED_FOLDERS = {
    "__pycache__",
    ".venv",
    "venv",
    ".git",
    ".idea",
    ".pytest_cache",
    "data"  # evita que intente cargar json como módulos
}

EXCLUDED_FILES = {
    "main.py"
}

# ==============================
# LOADER DINÁMICO TOTAL
# ==============================

def load_system_modules():
    loaded = []
    errors = []

    for root, dirs, files in os.walk(BASE_DIR):

        # excluir carpetas no válidas
        dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]

        for file in files:

            if not file.endswith(".py"):
                continue

            if file.startswith("__"):
                continue

            if file in EXCLUDED_FILES:
                continue

            full_path = os.path.join(root, file)

            # Construir nombre de módulo absoluto correcto
            rel_path = os.path.relpath(full_path, BASE_DIR)
            module_name = rel_path.replace(os.sep, ".").replace(".py", "")

            try:
                module = importlib.import_module(module_name)
                
                # ÚNICO AGREGADO: Conecta tus rutas automáticamente para que funcionen
                if hasattr(module, "router"):
                    app.include_router(module.router)
                
                loaded.append(module_name)
            except Exception as e:
                errors.append({
                    "module": module_name,
                    "error": str(e)
                })

    return {
        "status": "BOOT_COMPLETED",
        "total_loaded": len(loaded),
        "total_errors": len(errors),
        "loaded": loaded,
        "errors": errors
    }

# ==============================
# ROOT
# ==============================

@app.get("/")
def root():
    return {
        "system": "ZYRA_NEXO_CORE",
        "status": "running",
        "environment": "PRODUCTION"
    }

# ==============================
# BOOT ENDPOINT
# ==============================

@app.get("/core/boot")
def boot_system():
    return load_system_modules()
