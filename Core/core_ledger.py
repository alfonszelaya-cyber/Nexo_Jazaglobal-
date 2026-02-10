# ============================================================
# core_ledger.py
# NEXO / ZYRA — LEDGER CORE (CANÓNICO)
# Núcleo contable + fiscal + auditoría
# Inmutable | Audit-ready | Long-term
# ============================================================

import json
import os
from datetime import datetime

# ===============================
# CONFIGURACIÓN BASE
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LEDGER_FILE = os.path.join(DATA_DIR, "ledger_core.json")

os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(LEDGER_FILE):
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# ===============================
# UTILIDADES INTERNAS
# ===============================

def _load_ledger():
    try:
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except Exception:
        pass
    return []

def _save_ledger(data):
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def _now():
    return datetime.utcnow().isoformat()

# ===============================
# REGISTRO CANÓNICO DE EVENTOS
# ===============================

def ledger_record(evento, estado, payload=None, origen="SYSTEM"):
    """
    Registra un hecho INMUTABLE del sistema

    evento  -> nombre del evento (VENTA, POS, DECLARACION, BLOQUEO, etc)
    estado  -> RECEIVED | OK | ERROR | BLOCKED | EMITIDO | CONFIRMADO
    payload -> datos relevantes (dict)
    origen  -> módulo que originó el evento
    """

    registro = {
        "timestamp": _now(),
        "evento": evento,
        "estado": estado,
        "origen": origen,
        "payload": payload or {}
    }

    data = _load_ledger()
    data.append(registro)
    _save_ledger(data)

    return registro

# ===============================
# CONSULTAS BÁSICAS (LECTURA)
# ===============================

def ledger_all():
    return _load_ledger()

def ledger_por_evento(evento):
    return [r for r in _load_ledger() if r.get("evento") == evento]

def ledger_por_estado(estado):
    return [r for r in _load_ledger() if r.get("estado") == estado]

def ledger_por_rango(fecha_inicio, fecha_fin):
    out = []
    for r in _load_ledger():
        ts = r.get("timestamp")
        if ts and fecha_inicio <= ts <= fecha_fin:
            out.append(r)
    return out

# ===============================
# BLOQUEOS / AUDITORÍA
# ===============================

def ledger_bloqueo(nivel, motivo, referencia=None):
    return ledger_record(
        evento="BLOQUEO",
        estado=f"NIVEL_{nivel}",
        payload={
            "motivo": motivo,
            "referencia": referencia
        },
        origen="SECURITY"
    )

def ledger_auditoria(mensaje, evidencia=None):
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
# PRUEBA LOCAL (OPCIONAL)
# ===============================

if __name__ == "__main__":
    ledger_record(
        evento="TEST_CORE",
        estado="OK",
        payload={"msg": "core_ledger operativo"},
        origen="CORE"
    )
    print("✔ core_ledger activo")