from fastapi import FastAPI
import os
import sys
import importlib

# ==============================
# CONFIGURACIÓN BASE SEGURA
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Asegurar que la raíz esté en el path para importaciones relativas
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

app = FastAPI(title="ZYRA NEXO CORE")

# ==============================
# CONFIGURACIÓN DE EXCLUSIONES
# ==============================
EXCLUDED_FOLDERS = {"__pycache__", ".venv", "venv", ".git", "data", "app"} # Se agregó 'app' si ya existe
EXCLUDED_FILES = {"main.py", "__init__.py"}

# ==============================
# LOADER DINÁMICO TOTAL
# ==============================
def load_system_modules():
    loaded = []
    errors = []

    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]

        for file in files:
            if not file.endswith(".py") or file in EXCLUDED_FILES or file.startswith("__"):
                continue

            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            
            # Convierte ruta de carpeta a formato de módulo Python (puntos)
            module_name = rel_path.replace(os.sep, ".").replace(".py", "")

            try:
                # Importación dinámica
                module = importlib.import_module(module_name)
                
                # Si el módulo tiene un router de FastAPI, lo incluimos automáticamente
                if hasattr(module, "router"):
                    app.include_router(module.router)
                
                loaded.append(module_name)
            except Exception as e:
                errors.append({"module": module_name, "error": str(e)})

    return {
        "status": "BOOT_COMPLETED",
        "total_loaded": len(loaded),
        "total_errors": len(errors),
        "errors": errors
    }

@app.get("/")
def root():
    return {"system": "ZYRA_NEXO_CORE", "status": "running"}

@app.get("/core/boot")
def boot_system():
    return load_system_modules()
