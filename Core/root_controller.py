# ============================================================
# SYSTEM STATE UPDATE (COMPATIBLE CON SYSTEM SERVICE)
# ============================================================

from datetime import datetime, timezone

_SYSTEM_STATE = {
    "state": "READY",
    "last_update": datetime.now(timezone.utc).isoformat()
}

def system_state_update(new_state: str) -> dict:
    """
    Actualiza el estado global del sistema.
    Compatible con SystemService.
    """

    _SYSTEM_STATE["state"] = new_state
    _SYSTEM_STATE["last_update"] = datetime.now(timezone.utc).isoformat()

    ledger_record(f"SYSTEM_STATE_UPDATED -> {new_state}")

    return {
        "system_name": "ZYRA_CORE",
        "version": "3.0.0",
        "state": _SYSTEM_STATE["state"],
        "timestamp": _SYSTEM_STATE["last_update"]
    }


# ============================================================
# SYSTEM STATE READ
# ============================================================

def get_system_state() -> dict:
    return {
        "system_name": "ZYRA_CORE",
        "version": "3.0.0",
        "state": _SYSTEM_STATE["state"],
        "timestamp": _SYSTEM_STATE["last_update"]
    }
