# ============================================================
# integrity_checker.py
# NEXO / ZYRA — VERIFICADOR DE INTEGRIDAD DEL CORE
# CORE | Pre-Boot | Auditoría | Inmutable
# ============================================================

import os
import json
import hashlib
from datetime import datetime

# ============================================================
# CONFIGURACIÓN DE PERSISTENCIA
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

INTEGRITY_FILE = os.path.join(DATA_DIR, "integrity.json")

if not os.path.exists(INTEGRITY_FILE):
    with open(INTEGRITY_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# ============================================================
# FUNCIONES DE HASH Y REGISTRO
# ============================================================

def calculate_hash(data: str) -> str:
    """Calcula hash SHA256 de un string"""
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def add_integrity_entry(file_name: str, content: str):
    """Registra la integridad de un archivo o entrada"""
    timestamp = datetime.utcnow().isoformat()
    hash_value = calculate_hash(content)

    entry = {
        "file_name": file_name,
        "hash": hash_value,
        "timestamp": timestamp
    }

    try:
        with open(INTEGRITY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []

    data.append(entry)

    try:
        with open(INTEGRITY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass


def verify_integrity(file_name: str, content: str) -> bool:
    """Verifica si la integridad de un archivo coincide con el registro"""
    hash_value = calculate_hash(content)

    try:
        with open(INTEGRITY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return False
    except Exception:
        return False

    for entry in data:
        if entry.get("file_name") == file_name and entry.get("hash") == hash_value:
            return True

    return False

# ============================================================
# ARCHIVOS CRÍTICOS DEL CORE
# ============================================================

CORE_FILES = [
    "core_contracts.py",
    "event_schema.py",
    "payload_validator.py",
    "system_state.py",
    "system_constants.py",
    "core_version.py",
    "version_registry.py",
    "integrity_checker.py",
    "boot_integrity_check.py",
    "zyra_exceptions.py",
    "error_handler.py",
    "shutdown.py",
    "health_check.py",
    "core_identity.py",
    "safe_mode.py",
    "boot_controller.py",
    "core_metrics.py",
    "core_ready_flag.py"
]

# ============================================================
# CHECK DE INTEGRIDAD DEL CORE
# ============================================================

def _hash_file(path: str) -> str:
    """Calcula SHA256 de un archivo"""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def check_core_integrity(base_dir: str = None) -> dict:
    """
    Verifica todos los archivos críticos del CORE
    Retorna:
    {
        "status": "OK" | "ERROR",
        "missing": [],
        "hashes": {file_name: hash}
    }
    """
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    missing = []
    hashes = {}

    for fname in CORE_FILES:
        fpath = os.path.join(base_dir, fname)
        if not os.path.exists(fpath):
            missing.append(fname)
        else:
            try:
                hashes[fname] = _hash_file(fpath)
            except Exception:
                missing.append(fname)

    status = "OK" if not missing else "ERROR"
    return {
        "status": status,
        "missing": missing,
        "hashes": hashes
    }

# ============================================================
# CHEQUEO DE BOOT / ARRANQUE
# ============================================================

BOOT_OK = "BOOT_OK"
BOOT_SAFE = "BOOT_SAFE"
BOOT_HALT = "BOOT_HALT"


def run_boot_integrity(base_dir: str = None) -> dict:
    """
    Chequeo de integridad al inicio
    Retorna:
    {
        "boot": BOOT_OK | BOOT_SAFE | BOOT_HALT,
        "integrity": {...}
    }
    """
    integrity = check_core_integrity(base_dir)

    if integrity["status"] == "OK":
        boot_status = BOOT_OK
    else:
        boot_status = BOOT_SAFE if integrity["missing"] else BOOT_HALT

    return {
        "boot": boot_status,
        "integrity": integrity
    }

# ============================================================
# NOTAS DE DISEÑO
# ============================================================
# - NO imprime
# - NO realiza tests
# - NO modifica estado global
# - Compatible con SAFE / DEGRADED MODE
# - Boot controller decide acción final
# ============================================================