# ============================================================
# system_constants.py
# NEXO / ZYRA — CONSTANTES GLOBALES DEL CORE
# CANÓNICO | INMUTABLE | 10+ AÑOS
# ============================================================
# No ejecuta lógica
# Solo define constantes universales
# ============================================================

from enum import Enum

# -------------------------
# IDENTIDAD DEL SISTEMA
# -------------------------
SYSTEM_NAME = "NEXO_ZYRA_CORE"
SYSTEM_SCHEMA_VERSION = "1"
CORE_VERSION = "1.0.0"

CORE_NAME = "NEXO / ZYRA"
CORE_LAYER = "CORE"
CORE_TYPE = "UNIFIED_SYSTEM"

# -------------------------
# ENTORNOS SOPORTADOS
# -------------------------
ENV_DEV = "DEV"
ENV_TEST = "TEST"
ENV_PROD = "PROD"
SUPPORTED_ENVIRONMENTS = [ENV_DEV, ENV_TEST, ENV_PROD]

# -------------------------
# MODOS DE OPERACIÓN
# -------------------------
MODE_NORMAL = "NORMAL"
MODE_SAFE = "SAFE"
MODE_DEGRADED = "DEGRADED"

# -------------------------
# ESTADOS DEL CORE
# -------------------------
STATE_BOOTING = "BOOTING"
STATE_READY = "READY"
STATE_SAFE = "SAFE"
STATE_DEGRADED = "DEGRADED"
STATE_LOCKED = "LOCKED"
STATE_SHUTDOWN = "SHUTDOWN"

# -------------------------
# NIVELES DE LOG / SEVERIDAD
# -------------------------
LOG_INFO = "INFO"
LOG_WARN = "WARN"
LOG_ERROR = "ERROR"
LOG_CRITICAL = "CRITICAL"

SEVERITY_INFO = "INFO"
SEVERITY_WARNING = "WARNING"
SEVERITY_ERROR = "ERROR"
SEVERITY_CRITICAL = "CRITICAL"

# -------------------------
# EVENTOS INTERNOS DEL CORE
# -------------------------
EVENT_CORE_BOOT = "CORE_BOOT"
EVENT_CORE_READY = "CORE_READY"
EVENT_CORE_SAFE = "CORE_SAFE"
EVENT_CORE_DEGRADED = "CORE_DEGRADED"
EVENT_CORE_SHUTDOWN = "CORE_SHUTDOWN"

# -------------------------
# ROLES BASE (NO BORRAR)
# -------------------------
ROLE_ROOT = "ROOT"
ROLE_SYSTEM = "SYSTEM"
ROLE_CORPORATION = "CORPORATION"
ROLE_GOVERNMENT = "GOVERNMENT"
ROLE_USER = "USER"

# -------------------------
# FLAGS DE CONTROL
# -------------------------
FLAG_READ_ONLY = "READ_ONLY"
FLAG_FULL_LOCK = "FULL_LOCK"
FLAG_AUDIT_REQUIRED = "AUDIT_REQUIRED"
FLAG_EXTERNAL_OVERRIDE = "EXTERNAL_OVERRIDE"

FLAG_TRUE = True
FLAG_FALSE = False

# -------------------------
# TIMEOUTS BASE (segundos)
# -------------------------
TIMEOUT_DEFAULT = 30
TIMEOUT_CRITICAL = 10
TIMEOUT_NETWORK = 60

# -------------------------
# VALORES POR DEFECTO
# -------------------------
DEFAULT_COUNTRY = "GLOBAL"
DEFAULT_CURRENCY = "USD"
DEFAULT_TIMEZONE = "UTC"

# -------------------------
# ACCIONES SENSIBLES (PARA API / SUPER BÚNKER)
# -------------------------
class SensitiveAction(str, Enum):
    VIEW = "view"
    EXECUTE = "execute"
    MODIFY = "modify"
    DELETE = "delete"
    UNLOCK = "unlock"

    # ============================================================
# LEDGER CONFIGURATION
# ============================================================

LEDGER_FILE = "ledger.json"

# ============================================================
# NOTA
# - Este archivo es CANÓNICO
# - Todo el CORE lo importa
# - No debe tener lógica
# ============================================================
