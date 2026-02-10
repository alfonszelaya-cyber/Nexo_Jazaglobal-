# ============================================================
# events_catalog.py
# NEXO / ZYRA — EVENTOS UNIVERSALES CANÓNICOS
# Catálogo Maestro | Validación Estricta | Inmutable
# ============================================================

import uuid
from datetime import datetime

# ============================================================
# 1. CATÁLOGO DE EVENTOS AUTORIZADOS (UNIFICADO)
# ============================================================

EVENTOS_PERMITIDOS = {
    # --- SISTEMA CRÍTICO ---
    "CORE_INIT",
    "CORE_SHUTDOWN",
    "BLOQUEO_SEGURIDAD",
    "ALERTA_RIESGO",

    # --- FINANCIERO / NEXO ---
    "VENTA_POS",
    "VENTA_REGISTRADA",
    "VENTA_CANCELADA",
    "FACTURA_EMITIDA",
    "PAGO_RECIBIDO",
    "PAGO_INICIADO",
    "PAGO_CONFIRMADO",
    "PAGO_FALLIDO",
    "GASTO_OPERATIVO",
    "CIERRE_CAJA",
    "POS_CERRADO",

    # --- INVENTARIO / LOGÍSTICA ---
    "STOCK_ENTRADA",
    "STOCK_SALIDA",
    "INVENTARIO_ENTRADA",
    "INVENTARIO_SALIDA",
    "INVENTARIO_AJUSTADO",
    "STOCK_BAJO_DETECTADO",
    "IMPORTACION_ORDEN",
    "IMPORTACION_INICIADA",
    "IMPORTACION_EN_TRANSITO",
    "IMPORTACION_RECIBIDA",
    "ADUANA_LIBERACION",

    # --- FISCAL / CONTABLE ---
    "DOCUMENTO_SIMULADO",
    "DOCUMENTO_EMITIDO",
    "NOTA_CREDITO_EMITIDA",
    "DECLARACION_IVA",
    "DECLARACION_MENSUAL_GENERADA",
    "DECLARACION_MENSUAL_ENVIADA",
    "PAGO_IMPUESTO",
    "AUDITORIA_FISCAL",
    "CIERRE_MENSUAL",
    "CIERRE_ANUAL",

    # --- IDENTIDAD / SEGURIDAD ---
    "LOGIN_OK",
    "LOGIN_FAIL",
    "LOGIN_EXITOSO",
    "LOGIN_FALLIDO",
    "CREACION_USUARIO",
    "CAMBIO_ROL",
    "ACCESO_FALLIDO_REPETIDO",
    "ACCION_FUERA_DE_ROL",
    "RIESGO_ALTO_DETECTADO",
    "BLOQUEO_PREVENTIVO"
}

# ============================================================
# 2. CONSTRUCTOR DE EVENTOS CANÓNICOS
# ============================================================

def crear_evento_canonico(
    tipo: str,
    sector: str,
    pais: str,
    actor_id: str,
    payload: dict = None,
    criticidad: str = "NORMAL"
):
    """
    Construye un evento validado y listo para Ledger / EventBus
    """

    if not isinstance(tipo, str):
        raise ValueError("CRITICAL: tipo de evento inválido")

    tipo = tipo.strip().upper()

    if tipo not in EVENTOS_PERMITIDOS:
        raise ValueError(f"CRITICAL: Evento '{tipo}' no autorizado por el catálogo")

    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "tipo": tipo,
        "sector": sector,
        "pais": pais,
        "actor_id": actor_id,
        "criticidad": criticidad,
        "payload": payload or {}
    }

# ============================================================
# 3. UTILIDADES DE CONSULTA
# ============================================================

def es_evento_valido(tipo: str) -> bool:
    return isinstance(tipo, str) and tipo.strip().upper() in EVENTOS_PERMITIDOS

def listar_eventos_disponibles() -> list:
    return sorted(EVENTOS_PERMITIDOS)

# ============================================================
# REGLAS
# - main lo importa
# - No ejecuta nada solo
# - No imprime
# - Inmutable
# - 10+ años estable
# ============================================================