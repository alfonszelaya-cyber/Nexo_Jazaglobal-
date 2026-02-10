# ============================================================
# event_schema.py
# NEXO / ZYRA — EVENT SCHEMA CANÓNICO
# BASE INMUTABLE | VALIDACIÓN ESTRUCTURAL
# ============================================================
# Define la forma oficial de un evento del CORE
# NO ejecuta lógica
# NO valida contenido, solo estructura
# ============================================================

from typing import TypedDict, Optional, Any

# ============================================================
# DEFINICIÓN TIPADA (ESTRUCTURA PYTHON)
# ============================================================

class EventPayload(TypedDict):
    event: str
    source: str
    timestamp: Optional[str]
    payload: Optional[Any]


class EventRecord(TypedDict):
    id: str
    payload: EventPayload
    status: str  # PENDIENTE, PROCESADO, ERROR
    metadata: Optional[dict]


# ============================================================
# ESQUEMA CANÓNICO (MAPA DE VALIDACIÓN)
# ============================================================

EVENT_SCHEMA = {

    "event_id": {
        "type": "UUID",
        "required": True,
        "descripcion": "Identificador único del evento"
    },

    "tipo": {
        "type": "STRING",
        "required": True,
        "descripcion": "Tipo canónico del evento"
    },

    "origen": {
        "type": "STRING",
        "required": True,
        "descripcion": "Módulo o actor que emite el evento"
    },

    "sector": {
        "type": "STRING",
        "required": False,
        "descripcion": "Sector funcional (FINANZAS, INVENTARIO, etc)"
    },

    "pais": {
        "type": "STRING",
        "required": False,
        "descripcion": "Código de país (ISO)"
    },

    "criticidad": {
        "type": "ENUM",
        "values": ["NORMAL", "ALTA", "CRITICA"],
        "required": True,
        "descripcion": "Nivel de impacto del evento"
    },

    "payload": {
        "type": "DICT",
        "required": True,
        "descripcion": "Datos asociados al evento"
    },

    "timestamp": {
        "type": "ISO_DATETIME",
        "required": True,
        "descripcion": "Fecha/hora UTC de creación"
    }
}

# ============================================================
# REGLAS
# - Todo evento del CORE debe cumplir este esquema
# - El validador vive en payload_validator.py
# - Este archivo NO ejecuta nada
# - main solo lo importa
# - No debe modificarse sin orden explícita
# ============================================================