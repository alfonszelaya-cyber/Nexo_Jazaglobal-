# ============================================================
# ZYRA / NEXO
# MAIN ENTRYPOINT — ENTERPRISE 3.0
# Dynamic Loader + API Bootstrap + Security Layer
# ============================================================

from fastapi import FastAPI
import os
import sys
import importlib
import secrets
import string
import uuid
import hashlib
from datetime import datetime, timedelta

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
# AUTO REGISTER ROUTERS
# ============================================================

try:
    from app.router import router as api_router
    app.include_router(api_router)
except Exception:
    pass


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
# HEALTH
# ============================================================

@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "timestamp": datetime.utcnow()
    }


# ============================================================
# BOOT
# ============================================================

@app.get("/core/boot")
def boot_system():
    return load_system_modules()


# ============================================================
# SECURITY TOOLS — ENTERPRISE
# ============================================================

# 🔐 Generar contraseña segura
@app.get("/security/generate-password")
def generate_password(length: int = 16):

    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))

    return {
        "generated_password": password,
        "length": length
    }


# 🎟 Generar token seguro
@app.get("/security/generate-token")
def generate_token(length: int = 32):

    token = secrets.token_hex(length)

    return {
        "secure_token": token,
        "expires_in_minutes": 60
    }


# 🔢 Generar número seguro
@app.get("/security/generate-number")
def generate_secure_number(digits: int = 8):

    number = ''.join(secrets.choice(string.digits) for _ in range(digits))

    return {
        "secure_number": number
    }


# 🆔 Generar UUID
@app.get("/security/generate-uuid")
def generate_uuid():

    return {
        "uuid": str(uuid.uuid4())
    }


# 🔒 Hash SHA256
@app.post("/security/hash")
def hash_data(payload: dict):

    if "data" not in payload:
        return {"error": "data field required"}

    hashed = hashlib.sha256(payload["data"].encode()).hexdigest()

    return {
        "original": payload["data"],
        "sha256": hashed
    }


# ============================================================
# FUTURE ZONE
# ============================================================

@app.get("/core/info")
def system_info():
    return {
        "architecture": "Clean Architecture",
        "environment": os.getenv("ENVIRONMENT", "production"),
        "modules_path": BASE_DIR
    }
