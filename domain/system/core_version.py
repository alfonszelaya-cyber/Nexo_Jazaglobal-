# ============================================================
# core_version.py
# NEXO / ZYRA — VERSIÓN CANÓNICA DEL CORE
# INMUTABLE | SELLADO | AUDITABLE | 10+ AÑOS
# ============================================================
# Fuente ÚNICA de verdad de la versión del CORE
# El sistema solo LEE este archivo, nunca lo modifica.
# ============================================================

from datetime import datetime

# -------------------------
# IDENTIDAD DE VERSIÓN
# -------------------------
CORE_VERSION = "1.0.0"
CORE_CODENAME = "ZYRA_GENESIS"
CORE_STAGE = "SEALED"   # DEV | RC | SEALED

# -------------------------
# METADATA DE RELEASE
# -------------------------
VERSION_RELEASE_DATE = "2026-01-30"
VERSION_TIMESTAMP = datetime.utcnow().isoformat()

# -------------------------
# COMPATIBILIDAD
# -------------------------
MIN_PYTHON_VERSION = "3.10"
ARCH_COMPATIBILITY = "x86_64 | arm64"

# -------------------------
# BLOQUEO
# -------------------------
VERSION_LOCKED = True   # No se permite cambio en caliente

# ============================================================
# REGISTRO CANÓNICO DE VERSIONES
# ============================================================
# Solo se agregan versiones cuando se hace un release real.
# ============================================================

VERSION_REGISTRY = [
    {
        "version": CORE_VERSION,
        "codename": CORE_CODENAME,
        "stage": CORE_STAGE,
        "released_at": VERSION_TIMESTAMP,
        "sealed": True,
        "notes": "Versión base sellada del CORE ZYRA/NEXO"
    }
]

# ============================================================
# FUNCIONES DE CONSULTA (LECTURA בלבד)
# ============================================================

def get_current_version():
    """Devuelve la versión actual del CORE"""
    return VERSION_REGISTRY[-1]

def list_versions():
    """Devuelve historial completo de versiones"""
    return VERSION_REGISTRY

def get_core_identity():
    """Devuelve identidad completa del CORE"""
    return {
        "version": CORE_VERSION,
        "codename": CORE_CODENAME,
        "stage": CORE_STAGE,
        "released": VERSION_RELEASE_DATE,
        "arch": ARCH_COMPATIBILITY,
        "python_min": MIN_PYTHON_VERSION,
        "locked": VERSION_LOCKED
    }

# ============================================================
# NOTAS DE DISEÑO
# ============================================================
# - NO escribe archivos
# - NO modifica estado
# - NO depende de JSON
# - Compatible con auditoría legal
# - Boot puede validar contra esto
# - Duración: 10+ años
# ============================================================