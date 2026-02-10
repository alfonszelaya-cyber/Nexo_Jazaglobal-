

# ============================================================
# zyra_exceptions.py
# Excepciones específicas del CORE ZYRA
# ============================================================

class ZyraException(Exception):
    """Excepción base para errores del CORE"""
    pass

class DocumentValidationError(ZyraException):
    """Error al validar documentos"""
    pass

class LedgerWriteError(ZyraException):
    """Error al escribir en el ledger"""
    pass

class EventDispatchError(ZyraException):
    """Error al despachar eventos"""
    pass

class BootError(ZyraException):
    """Error durante el arranque del CORE"""
    pass

class SafeModeError(ZyraException):
    """Error crítico que fuerza modo seguro"""
    pass
    
    
    
    # ============================================================
# zyra_exceptions.py
# NEXO / ZYRA — EXCEPCIONES CANÓNICAS DEL CORE
# Inmutable | CORE
# ============================================================

class ZyraCoreError(Exception):
    """Excepción base del CORE ZYRA"""
    code = "CORE_ERROR"
    fatal = False

    def __init__(self, message=None, detail=None):
        super().__init__(message or self.code)
        self.message = message or self.code
        self.detail = detail

    def to_dict(self):
        return {
            "error": self.code,
            "message": self.message,
            "fatal": self.fatal,
            "detail": self.detail
        }


# -------------------------
# ERRORES CRÍTICOS
# -------------------------
class CoreBootError(ZyraCoreError):
    code = "CORE_BOOT_ERROR"
    fatal = True


class CoreIntegrityError(ZyraCoreError):
    code = "CORE_INTEGRITY_ERROR"
    fatal = True


class CoreConfigError(ZyraCoreError):
    code = "CORE_CONFIG_ERROR"
    fatal = True


# -------------------------
# ERRORES OPERATIVOS
# -------------------------
class LedgerError(ZyraCoreError):
    code = "LEDGER_ERROR"


class EventBusError(ZyraCoreError):
    code = "EVENT_BUS_ERROR"


class LogSystemError(ZyraCoreError):
    code = "LOG_SYSTEM_ERROR"


class ValidationError(ZyraCoreError):
    code = "VALIDATION_ERROR"


class ContractViolationError(ZyraCoreError):
    code = "CONTRACT_VIOLATION"


# -------------------------
# MODOS DEL SISTEMA
# -------------------------
class SafeModeActivated(ZyraCoreError):
    code = "SAFE_MODE"
    fatal = False


class DegradedModeActivated(ZyraCoreError):
    code = "DEGRADED_MODE"
    fatal = False


# ============================================================
# NOTA
# - NO ejecuta lógica
# - SOLO define tipos de error
# - Usado por error_handler, boot, health, router
# ============================================================