# ============================================================
# accounting_engine.py
# NEXO / ZYRA — MOTOR CONTABLE UNIVERSAL
# Event-driven | Multipaís | Inmutable | CORE
# ============================================================

import os
import json
import uuid
from datetime import datetime

# -----------------------------
# CONFIGURACIÓN DE RUTAS
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

LEDGER_FILE = os.path.join(DATA_DIR, "ledger.json")

# -----------------------------
# UTILIDADES SEGURAS
# -----------------------------
def _now():
    return datetime.utcnow().isoformat()

def _uid():
    return str(uuid.uuid4())

def _load(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# -----------------------------
# REGISTRO CONTABLE CANÓNICO
# -----------------------------
def registrar_evento_contable(event_type, data):
    """
    Registra un movimiento contable oficial.
    data requerido:
    {
        "empresa_id": "EMP-001",
        "pais": "SV",
        "monto": 113.00,
        "moneda": "USD",
        "cuenta_debito": "CAJA",
        "cuenta_credito": "INGRESOS",
        "ref": "POS-001"
    }
    """
    
    # Validación básica
    required = ["empresa_id", "pais", "monto", "cuenta_debito", "cuenta_credito"]
    for field in required:
        if field not in data:
            raise ValueError(f"Falta campo contable obligatorio: {field}")

    asiento = {
        "asiento_id": _uid(),
        "evento": event_type,
        "empresa_id": data["empresa_id"],
        "pais": data["pais"],
        "debito": data["cuenta_debito"],
        "credito": data["cuenta_credito"],
        "monto": float(data["monto"]),
        "moneda": data.get("moneda", "USD"),
        "referencia": data.get("ref", "S/R"),
        "timestamp": _now()
    }

    ledger = _load(LEDGER_FILE)
    ledger.append(asiento)
    _save(LEDGER_FILE, ledger)

    print(f"[ACCOUNTING] Asiento registrado: {asiento['asiento_id']}")
    return asiento

# -----------------------------
# CONSULTAS CONTABLES
# -----------------------------
def libro_por_empresa(empresa_id):
    ledger = _load(LEDGER_FILE)
    return [a for a in ledger if a.get("empresa_id") == empresa_id]

def libro_por_pais(pais):
    ledger = _load(LEDGER_FILE)
    return [a for a in ledger if a.get("pais") == pais]

# -----------------------------
# PRUEBA LOCAL CONTROLADA
# -----------------------------
if __name__ == "__main__":
    print("--- TEST ACCOUNTING ENGINE ---")
    
    try:
        asiento = registrar_evento_contable(
            "VENTA",
            {
                "empresa_id": "EMP-TEST",
                "pais": "SV",
                "monto": 100.00,
                "moneda": "USD",
                "cuenta_debito": "CAJA_GENERAL",
                "cuenta_credito": "INGRESOS_VENTAS",
                "ref": "TICKET-001"
            }
        )
        print("✔ OK:", asiento)
    except Exception as e:
        print("✘ ERROR:", e)
