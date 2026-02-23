# ============================================================
# NEXO / ZYRA — EVENT ROUTER (BASE DEFINITIVA / GOLDEN)
# Inmutable | Event-driven | Multimódulo | JAZA GLOBAL
# ============================================================

import os
import json
from datetime import datetime

# -----------------------------
# CONFIGURACIÓN DE RUTAS Y DATOS
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

EVENTS_FILE = os.path.join(DATA_DIR, "events.json")
LEDGER_FILE = os.path.join(DATA_DIR, "ledger.json")
LOGS_FILE = os.path.join(DATA_DIR, "logs.json")

# -----------------------------
# UTILIDADES DE PERSISTENCIA
# -----------------------------
def _now():
    return datetime.utcnow().isoformat()

def _load(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else default
    except Exception:
        return default

def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# -----------------------------
# CATÁLOGO CANÓNICO DE EVENTOS
# -----------------------------
EVENT_CATALOG = {
    "VENTA":              ["FINANZAS", "INVENTARIO", "FISCAL", "RADAR"],
    "COMPRA":             ["FINANZAS", "INVENTARIO", "FISCAL"],
    "IMPORTACION":        ["OPERACIONES", "FINANZAS", "FISCAL", "RADAR"],
    "EXPORTACION":        ["OPERACIONES", "FINANZAS", "FISCAL", "RADAR"],
    "PAGO":               ["FINANZAS", "TESORERIA"],
    "COBRO":              ["FINANZAS", "TESORERIA"],
    "AJUSTE":             ["FINANZAS", "INVENTARIO", "AUDITORIA"],
    "INVENTARIO_ENTRADA": ["INVENTARIO", "OPERACIONES"],
    "INVENTARIO_SALIDA":  ["INVENTARIO", "OPERACIONES"],
    "FACTURA_EMITIDA":    ["FINANZAS", "FISCAL", "LEGAL"],
    "FACTURA_RECIBIDA":   ["FINANZAS", "FISCAL"],
    "DECLARACION_FISCAL": ["FISCAL", "GOBIERNO"],
    "ALERTA_ZYRA":        ["AUDITORIA", "RIESGOS"],
    "DECISION_ZYRA":      ["AUDITORIA", "CORE"],

    # 🔐 AUTH EVENTS (AGREGADO CORRECTAMENTE)
    "LOGIN":              ["AUDITORIA"],
    "LOGOUT":             ["AUDITORIA"],
    "TOKEN_VALIDATED":    ["AUDITORIA"]
}

# -----------------------------
# ROUTER PRINCIPAL
# -----------------------------
def route_event(event_type, payload, source="SYSTEM"):

    if event_type not in EVENT_CATALOG:
        raise ValueError(f"Evento no permitido en CORE: {event_type}")

    ts = _now()
    impacted_modules = EVENT_CATALOG[event_type]

    # Registro maestro de eventos
    events = _load(EVENTS_FILE, [])
    events.append({
        "event": event_type,
        "source": source,
        "modules": impacted_modules,
        "payload": payload,
        "ts": ts
    })
    _save(EVENTS_FILE, events)

    # Ledger financiero automático
    if "FINANZAS" in impacted_modules and isinstance(payload, dict):
        monto = payload.get("monto_usd")
        if monto is not None:
            ledger = _load(LEDGER_FILE, [])
            ledger.append({
                "ref": payload.get("id", "N/A"),
                "tipo": event_type,
                "monto_usd": monto,
                "descripcion": payload.get("descripcion", event_type),
                "fecha": ts,
                "auditoria_hash": "PENDIENTE_FIRMADO"
            })
            _save(LEDGER_FILE, ledger)

    # Log técnico
    logs = _load(LOGS_FILE, [])
    logs.append({
        "level": "INFO",
        "event": event_type,
        "source": source,
        "modules": impacted_modules,
        "ref_id": payload.get("id") if isinstance(payload, dict) else None,
        "ts": ts
    })
    _save(LOGS_FILE, logs)

    # Disparadores ZYRA
    TRIGGERS = {
        "RADAR":      "EVALUAR_OPORTUNIDAD",
        "FISCAL":     "CALCULAR_IMPUESTOS",
        "INVENTARIO": "ACTUALIZAR_STOCK",
        "AUDITORIA":  "SELLADO_BLOCKCHAIN",
        "RIESGOS":    "ACTIVAR_PROTOCOLO_SEGURIDAD"
    }

    fired_actions = [TRIGGERS[m] for m in impacted_modules if m in TRIGGERS]

    return {
        "status": "OK",
        "event": event_type,
        "impact": impacted_modules,
        "zyra_actions": fired_actions,
        "timestamp": ts
    }
