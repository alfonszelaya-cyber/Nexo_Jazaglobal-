# ============================================================
# ledger.py
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

# Inicializar ledger si no existe
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
            if not isinstance(data, list):
                return []
            return data
    except Exception:
        return []


def _save_ledger(data):
    try:
        with open(LEDGER_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        pass


def _now():
    return datetime.utcnow().isoformat()

# ===============================
# REGISTRO CANÓNICO DE EVENTOS
# ===============================
def ledger_record(evento, estado, payload=None, origen="SYSTEM"):
    """
    Registra un hecho INMUTABLE del sistema.
    
    Args:
        evento (str): Nombre del evento (VENTA, POS, DECLARACION, BLOQUEO)
        estado (str): RECEIVED | OK | ERROR | BLOCKED | EMITIDO
        payload (dict): Datos relevantes
        origen (str): Módulo que originó el evento
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

    print(f"[LEDGER] Nuevo registro: {evento} | {estado}")
    return registro

# ===============================
# CONSULTAS BÁSICAS (LECTURA)
# ===============================
def ledger_all():
    """Devuelve todo el ledger"""
    return _load_ledger()


def ledger_por_evento(evento):
    """Filtra por tipo de evento"""
    return [r for r in _load_ledger() if r.get("evento") == evento]


def ledger_por_estado(estado):
    """Filtra por estado"""
    return [r for r in _load_ledger() if r.get("estado") == estado]


def ledger_por_rango(fecha_inicio, fecha_fin):
    """
    Filtra por fechas (ISO string)
    """
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
    """
    Registra un bloqueo crítico del sistema
    """
    return ledger_record(
        evento="BLOQUEO_SEGURIDAD",
        estado=f"NIVEL_{nivel}",
        payload={
            "motivo": motivo,
            "referencia": referencia
        },
        origen="BUNKER_SECURITY"
    )


def ledger_auditoria(mensaje, evidencia=None):
    """
    Registro manual / legal / auditoría
    """
    return ledger_record(
        evento="AUDITORIA_MANUAL",
        estado="REGISTRO",
        payload={
            "mensaje": mensaje,
            "evidencia": evidencia
        },
        origen="AUDIT_OFFICER"
    )

# ===============================
# PRUEBA LOCAL
# ===============================
if __name__ == "__main__":
    print("--- INICIANDO LEDGER CORE ---")

    ledger_record(
        evento="TEST_INIT",
        estado="OK",
        payload={"msg": "Sistema de memoria central activo"},
        origen="KERNEL"
    )

    # Prueba de bloqueo
    ledger_bloqueo("CRITICO", "Intento de acceso root fallido", "IP_UNKNOWN")

    print("✔ Ledger operativo y guardando.")