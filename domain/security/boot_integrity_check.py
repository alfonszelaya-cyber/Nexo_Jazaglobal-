# ============================================================
# boot_integrity_check.py
# NEXO / ZYRA — CHEQUEO DE INTEGRIDAD DE ARRANQUE
# CORE | PRE-BOOT | INMUTABLE | AUDITABLE | 10+ AÑOS
# ============================================================

from domain.security.integrity_checker import run_boot_integrity, BOOT_OK, BOOT_SAFE, BOOT_HALT
from datetime import datetime

# ============================================================
# ESTADO GLOBAL DE ARRANQUE
# ============================================================

BOOT_RESULT = None
BOOT_TIMESTAMP = None
BOOT_REPORT = None

# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================

def execute_boot_check(base_dir: str = None) -> dict:
    """
    Ejecuta el chequeo de integridad del CORE antes del arranque.

    Retorna:
    {
        "boot": BOOT_OK | BOOT_SAFE | BOOT_HALT,
        "integrity": {...},
        "timestamp": str
    }
    """
    global BOOT_RESULT, BOOT_TIMESTAMP, BOOT_REPORT

    result = run_boot_integrity(base_dir)

    BOOT_RESULT = result.get("boot")
    BOOT_TIMESTAMP = datetime.utcnow().isoformat()
    BOOT_REPORT = {
        "boot": BOOT_RESULT,
        "integrity": result.get("integrity"),
        "timestamp": BOOT_TIMESTAMP
    }

    return BOOT_REPORT

# ============================================================
# UTILIDADES DE CONSULTA
# ============================================================

def get_boot_status() -> str:
    """
    Devuelve el estado actual del boot:
    BOOT_OK | BOOT_SAFE | BOOT_HALT | NONE
    """
    return BOOT_RESULT or "NONE"

def is_boot_allowed() -> bool:
    """
    Indica si el sistema puede continuar arrancando.
    """
    return BOOT_RESULT in (BOOT_OK, BOOT_SAFE)

def get_boot_report() -> dict:
    """
    Devuelve el último reporte completo de integridad.
    """
    return BOOT_REPORT or {}

# ============================================================
# NOTAS DE DISEÑO
# ============================================================
# - NO imprime
# - NO detiene el sistema por sí solo
# - Boot_controller decide qué hacer
# - Compatible con SAFE MODE
# - Compatible con auditoría legal
# - Diseñado para 10+ años
# - Sin dependencias externas
# - CORE SILICON GRADE
# ============================================================
