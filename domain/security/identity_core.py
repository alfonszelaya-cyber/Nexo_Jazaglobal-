# ============================================================
# core_identity.py
# Gestión de identidad central del CORE ZYRA/NEXO
# ============================================================

import os
import json
import datetime
import uuid
from datetime import datetime as _dt

# -----------------------------
# Configuración del archivo de identidad
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
CORE_ID_FILE = os.path.join(DATA_DIR, "core_identity.json")

# Inicializar archivo si no existe
if not os.path.exists(CORE_ID_FILE):
    identity = {
        "core_id": str(uuid.uuid4()),
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(CORE_ID_FILE, "w", encoding="utf-8") as f:
        json.dump(identity, f, indent=2)
    print(f"[CORE_IDENTITY] Identidad inicial creada: {identity['core_id']}")

# -----------------------------
# Funciones de identidad (TU LÓGICA ORIGINAL)
# -----------------------------
def get_core_identity():
    """
    Retorna la identidad única del CORE
    """
    try:
        with open(CORE_ID_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("core_id")
    except Exception:
        return None


def reset_core_identity():
    """
    Resetea la identidad del CORE a un nuevo UUID
    """
    identity = {
        "core_id": str(uuid.uuid4()),
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        with open(CORE_ID_FILE, "w", encoding="utf-8") as f:
            json.dump(identity, f, indent=2)
        print(f"[CORE_IDENTITY] Identidad del CORE reseteada: {identity['core_id']}")
        return identity['core_id']
    except Exception as e:
        print(f"[CORE_IDENTITY] Error al resetear identidad: {e}")
        return None


# ============================================================
# IDENTIDAD CANÓNICA (TU SEGUNDA PARTE ORIGINAL)
# ============================================================

_CORE_ID = str(uuid.uuid4())
_SESSION_ID = str(uuid.uuid4())
_BOOT_TS = _dt.utcnow().isoformat()


def get_core_id():
    """ID único del CORE (vida del sistema)"""
    return _CORE_ID


def get_session_id():
    """ID único de esta ejecución"""
    return _SESSION_ID


def get_boot_timestamp():
    """Timestamp de inicio del CORE"""
    return _BOOT_TS


def core_identity():
    """Snapshot completo de identidad"""
    return {
        "core_id": _CORE_ID,
        "session_id": _SESSION_ID,
        "boot_ts": _BOOT_TS
    }


# ============================================================
# INYECCIÓN PARA API (SIN CAMBIAR TU LÓGICA)
# ============================================================

class IDENTITY_REGISTRY:
    def __init__(self):
        self.core_id = get_core_identity() or _CORE_ID
        self.session_id = _SESSION_ID
        self.boot_ts = _BOOT_TS

    def get_core_id(self):
        return self.core_id

    def get_session_id(self):
        return self.session_id

    def get_boot_timestamp(self):
        return self.boot_ts

    def snapshot(self):
        return {
            "core_id": self.core_id,
            "session_id": self.session_id,
            "boot_ts": self.boot_ts
        }

    def reset_core_identity(self):
        new_id = reset_core_identity()
        if new_id:
            self.core_id = new_id
        return self.core_id


# ============================================================
# NOTAS
# - NO se eliminó nada de tu lógica
# - Solo se inyectó compatibilidad con API
# - Listo para importarse como:
#   from core.identity_core import IDENTITY_REGISTRY
# ============================================================