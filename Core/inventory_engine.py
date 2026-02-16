# =========================================
# NEXO / ZYRA — INVENTARIO EVENT-BASED
# Inmutable | Auditable | Multisector | Largo Plazo
# =========================================

from datetime import datetime
import json
import os

# -------------------------
# PATHS
# -------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

EVENTS_FILE = os.path.join(DATA_DIR, "inventory_events.json")
STOCK_FILE = os.path.join(DATA_DIR, "inventory_stock.json")

# -------------------------
# UTILIDADES INTERNAS
# -------------------------

def _now():
    return datetime.utcnow().isoformat()


def _load(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return default


def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# -------------------------
# TIPOS DE EVENTO SOPORTADOS
# -------------------------

EVENT_TYPES = {
    "ENTRADA",
    "SALIDA",
    "AJUSTE",
    "BLOQUEO",
    "DESBLOQUEO"
}

# -------------------------
# REGISTRO DE EVENTOS
# -------------------------

def registrar_evento(evento: dict) -> dict:
    if evento.get("tipo") not in EVENT_TYPES:
        return {"status": "ERROR", "msg": "Tipo de evento inválido"}

    if "producto_id" not in evento:
        return {"status": "ERROR", "msg": "producto_id requerido"}

    eventos = _load(EVENTS_FILE, [])

    evento_registrado = {
        "producto_id": evento["producto_id"],
        "tipo": evento["tipo"],
        "cantidad": evento.get("cantidad", 0),
        "sector": evento.get("sector", "GENERAL"),
        "ref": evento.get("ref"),
        "ts": _now()
    }

    eventos.append(evento_registrado)
    _save(EVENTS_FILE, eventos)

    _reconstruir_stock(evento["producto_id"])

    return {
        "status": "OK",
        "evento": evento_registrado
    }

# -------------------------
# RECONSTRUCCIÓN DE STOCK
# -------------------------

def _reconstruir_stock(producto_id: str):
    eventos = _load(EVENTS_FILE, [])
    stock = _load(STOCK_FILE, {})

    cantidad = 0
    bloqueado = False

    for e in eventos:
        if e.get("producto_id") != producto_id:
            continue

        if e["tipo"] == "ENTRADA":
            cantidad += e.get("cantidad", 0)

        elif e["tipo"] == "SALIDA":
            cantidad -= e.get("cantidad", 0)

        elif e["tipo"] == "AJUSTE":
            cantidad = e.get("cantidad", 0)

        elif e["tipo"] == "BLOQUEO":
            bloqueado = True

        elif e["tipo"] == "DESBLOQUEO":
            bloqueado = False

    stock[producto_id] = {
        "producto_id": producto_id,
        "cantidad": cantidad,
        "bloqueado": bloqueado,
        "actualizado": _now()
    }

    _save(STOCK_FILE, stock)

# -------------------------
# CONSULTAS
# -------------------------

def obtener_stock(producto_id: str) -> dict:
    stock = _load(STOCK_FILE, {})
    return stock.get(producto_id, {
        "producto_id": producto_id,
        "cantidad": 0,
        "bloqueado": False
    })


def inventario_completo() -> dict:
    return _load(STOCK_FILE, {})


def historial_eventos(producto_id: str = None) -> list:
    eventos = _load(EVENTS_FILE, [])
    if producto_id:
        return [e for e in eventos if e.get("producto_id") == producto_id]
    return eventos

# -------------------------
# REGISTRO INICIAL EN CORE
# -------------------------

def register_product_in_core(producto_id: str) -> dict:

    stock = _load(STOCK_FILE, {})

    if producto_id not in stock:
        stock[producto_id] = {
            "producto_id": producto_id,
            "cantidad": 0,
            "bloqueado": False,
            "actualizado": _now()
        }
        _save(STOCK_FILE, stock)

    return {
        "status": "OK",
        "producto_id": producto_id
    }

# -------------------------
# UPDATE STOCK DESDE ROUTER
# -------------------------

def update_product_stock_in_core(producto_id: str, quantity_change: int) -> dict:
    """
    Actualiza stock usando el sistema de eventos.
    El router puede llamarlo directamente.
    """

    tipo_evento = "ENTRADA" if quantity_change >= 0 else "SALIDA"

    evento = {
        "producto_id": producto_id,
        "tipo": tipo_evento,
        "cantidad": abs(quantity_change),
        "sector": "SYSTEM_UPDATE"
    }

    registrar_evento(evento)

    stock_actual = obtener_stock(producto_id)

    return {
        "status": "OK",
        "producto_id": producto_id,
        "new_stock": stock_actual.get("cantidad", 0)
    }
