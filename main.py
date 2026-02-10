from fastapi import FastAPI
import os
import sys
import importlib

# ==============================
# CONFIGURACIÓN BASE
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BASE_DIR, "Core")

sys.path.insert(0, BASE_DIR)

app = FastAPI(title="ZYRA NEXO CORE")

# ==============================
# LOADER DINÁMICO TOTAL DEL CORE
# ==============================

def load_core_modules():
    loaded = []
    errors = []

    for root, dirs, files in os.walk(CORE_DIR):
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

    return {"loaded": loaded, "errors": errors}


# ==============================
# ROOT
# ==============================

@app.get("/")
def root():
    return {
        "system": "ZYRA_NEXO_CORE",
        "status": "running"
    }

# ==============================
# BOOT ENDPOINT
# ==============================

@app.get("/core/boot")
def boot_core():
    return load_core_modules()
