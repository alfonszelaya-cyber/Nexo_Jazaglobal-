# ============================================================
# error_handler.py
# NEXO / ZYRA — ERROR CONTROLLER CANÓNICO
# CORE | INMUTABLE | 10+ AÑOS
# ============================================================

from zyra_exceptions import (
    ZyraCoreError,
    CoreBootError,
    CoreIntegrityError,
    LedgerError,
    EventBusError,
    LogSystemError,
    SafeModeActivated,
    DegradedModeActivated
)

from domain.security.safe_mode import (
    activate_safe_mode,
    activate_degraded_mode,
    restore_normal_mode,
    get_mode,
    MODE_SAFE,
    MODE_DEGRADED,
    MODE_NORMAL
)

# ------------------------------------------------------------
# HANDLER CENTRAL
# ------------------------------------------------------------
def handle_error(error, context: dict | None = None) -> dict:
    """
    Procesa cualquier excepción del CORE ZYRA
    - NO imprime
    - NO loggea
    - SOLO decide estado del sistema
    """

    # --------------------------------------------------------
    # Normalización
    # --------------------------------------------------------
    if not isinstance(error, ZyraCoreError):
        error = ZyraCoreError(
            message="UNHANDLED_EXCEPTION",
            detail=str(error)
        )

    payload = error.to_dict()
    payload["context"] = context or {}
    payload["previous_mode"] = get_mode()

    # --------------------------------------------------------
    # ERRORES FATALES → APAGADO
    # --------------------------------------------------------
    if error.fatal:
        payload["action"] = "SHUTDOWN_REQUIRED"
        payload["new_mode"] = get_mode()
        return payload

    # --------------------------------------------------------
    # ERRORES QUE DEGRADAN
    # --------------------------------------------------------
    if isinstance(error, (LedgerError, LogSystemError)):
        activate_degraded_mode(reason=error.code)
        payload["action"] = "DEGRADED_MODE"
        payload["new_mode"] = MODE_DEGRADED
        return payload

    # --------------------------------------------------------
    # ERRORES QUE AISLAN
    # --------------------------------------------------------
    if isinstance(error, EventBusError):
        activate_safe_mode(reason=error.code)
        payload["action"] = "SAFE_MODE"
        payload["new_mode"] = MODE_SAFE
        return payload

    # --------------------------------------------------------
    # EVENTOS DE CAMBIO DE ESTADO
    # --------------------------------------------------------
    if isinstance(error, (SafeModeActivated, DegradedModeActivated)):
        payload["action"] = error.code
        payload["new_mode"] = get_mode()
        return payload

    # --------------------------------------------------------
    # DEFAULT → IGNORADO
    # --------------------------------------------------------
    payload["action"] = "IGNORED"
    payload["new_mode"] = get_mode()
    return payload

# ============================================================
# NOTAS DE DISEÑO
# ============================================================
# - NO escribe archivos
# - NO depende de JSON
# - NO imprime
# - SOLO decide estados
# - Logger y EventBus consumen este payload
# - SafeMode es la única fuente de verdad del estado
# ============================================================
