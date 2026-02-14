# ============================================================
# core_ledger.py
# NEXO / ZYRA — LEDGER CORE (CANÓNICO ENTERPRISE 3.0)
# Núcleo contable + fiscal + auditoría
# Inmutable | Audit-ready | Long-term | 10+ años
# ============================================================

import json
import os
import threading
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any

# ===============================
# LOGGER CANÓNICO 3.0
# ===============================

def log(level: str, message: str) -> None:
    """
    Logger interno del CORE.
    - UTC ISO
    - Seguro en producción
    - No rompe ejecución
    """

    try:
        timestamp = datetime.now(timezone.utc).isoformat()
        print(f"[{timestamp}] [{level.upper()}] {message}")
    except Exception:
        pass


# ===============================
# CONFIGURACIÓN BASE
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LEDGER_FILE = os.path.join(DATA_DIR, "ledger_core.json")

os.makedirs(DATA_DIR, exist_ok=True)

# Lock para evitar corrupción por concurrencia
_LEDGER_LOCK = threading.Lock()

# Inicializar archivo si no existe
if not os.path.exists(LEDGER_FILE):
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)


# ===============================
# UTILIDADES INTERNAS
# ===============================

def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_ledger() -> List[Dict[str, Any]]:
    try:
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except Exception:
        log("ERROR", "Error cargando ledger")
    return []


def _save_ledger(data: List[Dict[str, Any]]) -> None:
    try:
        with open(LEDGER_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        log("CRITICAL", "Error guardando ledger")


# ===============================
# REGISTRO CANÓNICO (INMUTABLE)
# ===============================

def ledger_record(
    evento: str,
    estado: str,
    payload: Optional[Dict[str, Any]] = None,
    origen: str = "SYSTEM"
) -> Dict[str, Any]:

    registro = {
        "timestamp": _now(),
        "evento": str(evento),
        "estado": str(estado),
        "origen": str(origen),
        "payload": payload or {}
    }

    with _LEDGER_LOCK:
        data = _load_ledger()
        data.append(registro)
        _save_ledger(data)

    log("INFO", f"Ledger record creado: {evento}")

    return registro


# ===============================
# CONSULTAS (READ-ONLY)
# ===============================

def ledger_all() -> List[Dict[str, Any]]:
    return _load_ledger()


def ledger_por_evento(evento: str) -> List[Dict[str, Any]]:
    return [r for r in _load_ledger() if r.get("evento") == evento]


def ledger_por_estado(estado: str) -> List[Dict[str, Any]]:
    return [r for r in _load_ledger() if r.get("estado") == estado]


def ledger_por_origen(origen: str) -> List[Dict[str, Any]]:
    return [r for r in _load_ledger() if r.get("origen") == origen]


def ledger_por_rango(fecha_inicio: str, fecha_fin: str) -> List[Dict[str, Any]]:
    resultados = []
    for r in _load_ledger():
        ts = r.get("timestamp")
        if ts and fecha_inicio <= ts <= fecha_fin:
            resultados.append(r)
    return resultados


# ===============================
# SEGURIDAD / BLOQUEOS
# ===============================

def ledger_bloqueo(
    nivel: int,
    motivo: str,
    referencia: Optional[str] = None
) -> Dict[str, Any]:
    return ledger_record(
        evento="BLOQUEO",
        estado=f"NIVEL_{nivel}",
        payload={
            "motivo": motivo,
            "referencia": referencia
        },
        origen="SECURITY"
    )


def ledger_auditoria(
    mensaje: str,
    evidencia: Optional[Any] = None
) -> Dict[str, Any]:
    return ledger_record(
        evento="AUDITORIA",
        estado="REGISTRO",
        payload={
            "mensaje": mensaje,
            "evidencia": evidencia
        },
        origen="AUDIT"
    )


# ===============================
# MÉTRICAS BÁSICAS
# ===============================

def ledger_count() -> int:
    return len(_load_ledger())


def ledger_last() -> Optional[Dict[str, Any]]:
    data = _load_ledger()
    return data[-1] if data else None


# ===============================
# PRUEBA LOCAL CONTROLADA
# ===============================

if __name__ == "__main__":
    test = ledger_record(
        evento="TEST_CORE",
        estado="OK",
        payload={"msg": "core_ledger enterprise operativo"},
        origen="CORE"
    )
    print("✔ core_ledger enterprise activo")
    print(test)
