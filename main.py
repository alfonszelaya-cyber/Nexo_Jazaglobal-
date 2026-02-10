# ============================================================
# ZYRA / NEXO — API PRINCIPAL (Render Ready)
# ============================================================

import sys
import os
from fastapi import FastAPI

# ------------------------------------------------------------
# CONFIGURACIÓN DE RUTAS (inyectar Core al path)
# ------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_PATH = os.path.join(BASE_DIR, "Core")

if CORE_PATH not in sys.path:
    sys.path.append(CORE_PATH)

# ------------------------------------------------------------
# IMPORTACIÓN SEGURA DEL CORE
# ------------------------------------------------------------

try:
    from Core.health_check import run_health_check
    CORE_AVAILABLE = True
except Exception as e:
    CORE_AVAILABLE = False
    CORE_ERROR = str(e)

# ------------------------------------------------------------
# FASTAPI
# ------------------------------------------------------------

app = FastAPI(title="ZYRA NEXO CORE")

# ------------------------------------------------------------
# ROOT
# ------------------------------------------------------------

@app.get("/")
def root():
    return {
        "system": "ZYRA_NEXO_CORE",
        "status": "running"
    }

# ------------------------------------------------------------
# STATUS SIMPLE
# ------------------------------------------------------------

@app.get("/status")
def status():
    return {
        "core": "conectado" if CORE_AVAILABLE else "no disponible",
        "detalle": "Core cargado correctamente" if CORE_AVAILABLE else CORE_ERROR
    }

# ------------------------------------------------------------
# HEALTH REAL DEL CORE
# ------------------------------------------------------------

@app.get("/core/health")
def core_health():
    if CORE_AVAILABLE:
        return run_health_check()
    return {
        "error": "Core no disponible",
        "detalle": CORE_ERROR
    }
