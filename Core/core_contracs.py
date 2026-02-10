# ============================================================
# core_contracts.py
# Contratos base del CORE ZYRA
# ============================================================

from typing import Dict, Any

# ------------------------------------------------------------
# Contrato base de Documento
# ------------------------------------------------------------

DOCUMENT_CONTRACT: Dict[str, Any] = {
    "id": str,
    "tipo": str,
    "modulo": str,
    "pais": str,
    "estado": str,
    "fecha": str,        # ISO-8601
    "totales": {
        "subtotal": float,
        "impuestos": float,
        "total": float,
        "moneda": str
    },
    "metadata": dict
}

# ------------------------------------------------------------
# Contrato base de Evento
# ------------------------------------------------------------

EVENT_CONTRACT: Dict[str, Any] = {
    "id": str,
    "payload": dict,
    "status": str,       # PENDIENTE | PROCESADO | ERROR
    "description": str,
    "metadata": dict
}

# ------------------------------------------------------------
# Contrato base de Ledger
# ------------------------------------------------------------

LEDGER_ENTRY_CONTRACT: Dict[str, Any] = {
    "id": str,
    "tipo": str,
    "monto": float,
    "moneda": str,
    "timestamp": str,    # ISO-8601
    "metadata": dict
}

# ------------------------------------------------------------
# Validadores simples de contrato
# ------------------------------------------------------------

def validate_contract(data: dict, contract: Dict[str, Any]) -> bool:
    """
    Valida que un diccionario cumpla con un contrato base
    """
    for key, expected in contract.items():
        if key not in data:
            return False
        if isinstance(expected, dict):
            if not isinstance(data[key], dict):
                return False
            for subkey in expected:
                if subkey not in data[key]:
                    return False
    return True
    
    
    # ============================================================
# core_contracts.py
# NEXO / ZYRA — CORE CONTRACTS
# Contratos canónicos del sistema
# BASE INMUTABLE | 5+ AÑOS | CORE ONLY
# ============================================================
# Este archivo define:
# - Qué es el CORE
# - Qué se considera contrato del sistema
# - Qué reglas NO pueden romperse
# NO ejecuta lógica
# ============================================================


CORE_CONTRACTS = {

    # --------------------------------------------------------
    # IDENTIDAD DEL CORE
    # --------------------------------------------------------
    "CORE_IDENTITY": {
        "descripcion": "El CORE es único, central y autoritativo",
        "reglas": [
            "Existe un solo CORE activo",
            "Todo módulo depende del CORE",
            "El CORE no depende de módulos"
        ]
    },

    # --------------------------------------------------------
    # EVENTOS
    # --------------------------------------------------------
    "EVENT_CONTRACT": {
        "descripcion": "Todo evento debe ser canónico y validado",
        "reglas": [
            "Todo evento tiene tipo, origen y timestamp",
            "Eventos no se modifican una vez emitidos",
            "Eventos inválidos se rechazan"
        ]
    },

    # --------------------------------------------------------
    # LEDGER
    # --------------------------------------------------------
    "LEDGER_CONTRACT": {
        "descripcion": "El ledger es inmutable y auditable",
        "reglas": [
            "Nunca se edita un registro",
            "Solo se agregan entradas",
            "Errores también se registran"
        ]
    },

    # --------------------------------------------------------
    # ESTADO DEL SISTEMA
    # --------------------------------------------------------
    "SYSTEM_STATE_CONTRACT": {
        "descripcion": "El estado del CORE es explícito",
        "reglas": [
            "El CORE tiene estado definido",
            "SAFE y DEGRADED son estados válidos",
            "El CORE nunca opera sin estado"
        ]
    },

    # --------------------------------------------------------
    # INTEGRIDAD
    # --------------------------------------------------------
    "INTEGRITY_CONTRACT": {
        "descripcion": "La integridad se valida al arranque",
        "reglas": [
            "Archivos críticos deben existir",
            "Versiones deben coincidir",
            "Fallos activan SAFE o DEGRADED"
        ]
    },

    # --------------------------------------------------------
    # ERRORES
    # --------------------------------------------------------
    "ERROR_CONTRACT": {
        "descripcion": "Errores son ciudadanos de primera clase",
        "reglas": [
            "Errores tienen tipo canónico",
            "Errores se registran en ledger/logs",
            "Errores críticos pueden detener el CORE"
        ]
    },

    # --------------------------------------------------------
    # APAGADO
    # --------------------------------------------------------
    "SHUTDOWN_CONTRACT": {
        "descripcion": "El CORE siempre se cierra limpiamente",
        "reglas": [
            "Se registra el cierre",
            "Se preserva estado",
            "No se pierde información"
        ]
    }
}

# ============================================================
# NOTA FINAL
# - Los módulos consultan estos contratos
# - El CORE los hace cumplir
# - Este archivo NO se modifica
# ============================================================


# ============================================================
# core_contracts.py
# NEXO / ZYRA — CORE CONTRACTS
# Contratos canónicos del sistema
# BASE INMUTABLE | 5+ AÑOS | CORE ONLY
# ============================================================
# Este archivo define:
# - Qué es el CORE
# - Qué se considera contrato del sistema
# - Qué reglas NO pueden romperse
# NO ejecuta lógica
# ============================================================


CORE_CONTRACTS = {

    # --------------------------------------------------------
    # IDENTIDAD DEL CORE
    # --------------------------------------------------------
    "CORE_IDENTITY": {
        "descripcion": "El CORE es único, central y autoritativo",
        "reglas": [
            "Existe un solo CORE activo",
            "Todo módulo depende del CORE",
            "El CORE no depende de módulos"
        ]
    },

    # --------------------------------------------------------
    # EVENTOS
    # --------------------------------------------------------
    "EVENT_CONTRACT": {
        "descripcion": "Todo evento debe ser canónico y validado",
        "reglas": [
            "Todo evento tiene tipo, origen y timestamp",
            "Eventos no se modifican una vez emitidos",
            "Eventos inválidos se rechazan"
        ]
    },

    # --------------------------------------------------------
    # LEDGER
    # --------------------------------------------------------
    "LEDGER_CONTRACT": {
        "descripcion": "El ledger es inmutable y auditable",
        "reglas": [
            "Nunca se edita un registro",
            "Solo se agregan entradas",
            "Errores también se registran"
        ]
    },

    # --------------------------------------------------------
    # ESTADO DEL SISTEMA
    # --------------------------------------------------------
    "SYSTEM_STATE_CONTRACT": {
        "descripcion": "El estado del CORE es explícito",
        "reglas": [
            "El CORE tiene estado definido",
            "SAFE y DEGRADED son estados válidos",
            "El CORE nunca opera sin estado"
        ]
    },

    # --------------------------------------------------------
    # INTEGRIDAD
    # --------------------------------------------------------
    "INTEGRITY_CONTRACT": {
        "descripcion": "La integridad se valida al arranque",
        "reglas": [
            "Archivos críticos deben existir",
            "Versiones deben coincidir",
            "Fallos activan SAFE o DEGRADED"
        ]
    },

    # --------------------------------------------------------
    # ERRORES
    # --------------------------------------------------------
    "ERROR_CONTRACT": {
        "descripcion": "Errores son ciudadanos de primera clase",
        "reglas": [
            "Errores tienen tipo canónico",
            "Errores se registran en ledger/logs",
            "Errores críticos pueden detener el CORE"
        ]
    },

    # --------------------------------------------------------
    # APAGADO
    # --------------------------------------------------------
    "SHUTDOWN_CONTRACT": {
        "descripcion": "El CORE siempre se cierra limpiamente",
        "reglas": [
            "Se registra el cierre",
            "Se preserva estado",
            "No se pierde información"
        ]
    }
}

# ============================================================
# NOTA FINAL
# - Los módulos consultan estos contratos
# - El CORE los hace cumplir
# - Este archivo NO se modifica
# ============================================================