# zyra_core.py
# ZYRA CORE — NÚCLEO BASE SOBERANO

import time
from typing import Any, Dict, Optional

from core.zyra_ledger_hook import ledger_record
from core.zyra_bus import emit
from core.zyra_logs_hook import log

SYSTEM_STATE: Dict[str, Any] = {
    "boot_time": None,
    "events_count": 0
}

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
        event="CORE_BOOT",
        status="OK",
        detail="ZYRA CORE initialized"
    )

    emit(
        event="CORE_BOOT",
        source="ZYRA_CORE",
        payload={"status": "OK"}
    )


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
        event=name,
        status="RECORDED",
        detail=payload
    )

    emit(
        event=name,
        source=source,
        payload=payload
    )

    return evt


def get_core_state() -> Dict[str, Any]:
    return SYSTEM_STATE.copy()