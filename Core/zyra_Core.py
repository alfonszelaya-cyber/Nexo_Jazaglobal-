# zyra_core.py
# ZYRA CORE — NÚCLEO BASE SOBERANO

import time
from typing import Any, Dict, Optional

# ==============================
# IMPORTS CORRECTOS SEGÚN ESTRUCTURA REAL
# ==============================

from domain.finance.ledger import ledger_record
from infrastructure.events.zyra_bus import emit
from infrastructure.logging.zyra_logs_hook import log

# ==============================
# ESTADO DEL SISTEMA
# ==============================

SYSTEM_STATE: Dict[str, Any] = {
    "boot_time": None,
    "events_count": 0
}

# ==============================
# INICIALIZACIÓN DEL CORE
# ==============================

def zyra_core_init() -> None:
    if SYSTEM_STATE["boot_time"] is not None:
        return

    SYSTEM_STATE["boot_time"] = time.time()

    log(
        event="ZYRA CORE cargado",
        level="INFO",
        source="ZYRA_CORE"
    )

    ledger_record(
        evento="CORE_BOOT",
        estado="OK",
        payload={"detail": "ZYRA CORE initialized"},
        origen="ZYRA_CORE"
    )

    emit(
        event="CORE_BOOT",
        source="ZYRA_CORE",
        payload={"status": "OK"}
    )

# ==============================
# REGISTRO DE EVENTOS
# ==============================

def register_event(
    name: str,
    payload: Optional[Dict[str, Any]] = None,
    source: str = "UNKNOWN"
) -> Dict[str, Any]:

    evt = {
        "event": name,
        "source": source,
        "payload": payload,
        "ts": time.time()
    }

    SYSTEM_STATE["events_count"] += 1

    ledger_record(
        evento=name,
        estado="RECORDED",
        payload=payload,
        origen=source
    )

    emit(
        event=name,
        source=source,
        payload=payload
    )

    return evt

# ==============================
# CONSULTA DE ESTADO
# ==============================

def get_core_state() -> Dict[str, Any]:
    return SYSTEM_STATE.copy()
