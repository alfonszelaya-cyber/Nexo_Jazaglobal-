# =========================================
# operations_core.py
# NEXO / ZYRA — OPERATIONS CORE
# Base única de operaciones | Inmutable | Auditable | Event-driven | Largo plazo
# =========================================

from datetime import datetime
import json
import os
from uuid import uuid4

from infrastructure.zyra_bus import emit
from Core.core_ledger import ledger_record
from infrastructure.zyra_logs_hook import log

# -------------------------
# PATHS
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

OPERATIONS_FILE = os.path.join(DATA_DIR, "operations.json")

# -------------------------
# UTILIDADES
# -------------------------
def _now():
    return datetime.utcnow().isoformat()

def _load(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# -------------------------
# REGISTRO DE OPERACIÓN
# -------------------------
def registrar_operacion(
    tipo_operacion,
    monto,
    moneda="USD",
    origen=None,
    destino=None,
    estado="PENDIENTE",
    metadata=None
):
    """
    tipo_operacion: VENTA | COMPRA | TRANSFERENCIA | PAGO | COBRO | AJUSTE
    """
    operacion = {  
        "operation_id": f"OP-{uuid4().hex[:10].upper()}",  
        "tipo": tipo_operacion,  
        "monto": monto,  
        "moneda": moneda,  
        "origen": origen,  
        "destino": destino,  
        "estado": estado,  
        "metadata": metadata or {},  
        "ts": _now()  
    }  

    # Persistencia  
    operaciones = _load(OPERATIONS_FILE, [])  
    operaciones.append(operacion)  
    _save(OPERATIONS_FILE, operaciones)  

    # Ledger  
    ledger_record(  
        event="OPERACION_REGISTRADA",  
        status=estado,  
        detail=operacion  
    )  

    # Evento sistema  
    emit(  
        "OPERACION_REGISTRADA",  
        source="OPERATIONS_CORE",  
        payload={  
            "operation_id": operacion["operation_id"],  
            "tipo": tipo_operacion,  
            "monto": monto,  
            "moneda": moneda,  
            "estado": estado  
        }  
    )  

    # Log  
    log(  
        "INFO",  
        f"Operación {operacion['operation_id']} registrada",  
        "OPERATIONS_CORE"  
    )  

    return operacion

# -------------------------
# CONSULTAS
# -------------------------
def operaciones_por_tipo(tipo):
    return [o for o in _load(OPERATIONS_FILE, []) if o["tipo"] == tipo]

def operaciones_por_estado(estado):
    return [o for o in _load(OPERATIONS_FILE, []) if o["estado"] == estado]

def historial_operaciones():
    return _load(OPERATIONS_FILE, [])
