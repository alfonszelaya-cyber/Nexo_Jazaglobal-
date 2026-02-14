# =========================================
# pos_flow_engine.py
# NEXO / ZYRA — POS FLOW ENGINE
# Flujo operativo interno para eventos POS
# Event-driven | Auditable | Largo Plazo
# =========================================

from datetime import datetime

from Core.inventory_engine import registrar_evento as inventario_evento
from domain.finance.document_fiscal_engine import simular_documento, generar_documento
from Core.radar_engine import registrar_evento as radar_evento
from Core.core_ledger import ledger_record

# -------------------------
# PROCESAR EVENTO POS
# -------------------------
def procesar_venta_pos(evento: dict, documento: dict) -> dict:
    """
    evento    -> evento del dispatcher / bus
    documento -> estructura fiscal completa
    """

    # -------------------------
    # 1. INVENTARIO (SALIDA)
    # -------------------------
    for item in documento.get("items", []):
        inventario_evento({
            "producto_id": item["producto_id"],
            "tipo": "SALIDA",
            "cantidad": item["cantidad"],
            "sector": documento.get("sector"),
            "ref_evento": evento.get("id")
        })

    # -------------------------
    # 2. SIMULACIÓN FISCAL
    # -------------------------
    simulacion = simular_documento(documento)
    if not simulacion.get("valido"):
        return simulacion

    # -------------------------
    # 3. EMISIÓN DOCUMENTO
    # -------------------------
    factura = generar_documento(simulacion["preview"])

    # -------------------------
    # 4. RADAR (OBSERVACIÓN)
    # -------------------------
    radar_evento(
        tipo="VENTA_POS",
        origen="POS",
        descripcion=f"Venta POS confirmada {factura['doc_id']}",
        nivel=1,
        referencia=factura["doc_id"]
    )

    # -------------------------
    # 5. LEDGER (REGISTRO)
    # -------------------------
    ledger_record(
        event="VENTA_POS_CONFIRMADA",
        status="OK",
        detail={
            "evento_id": evento.get("id"),
            "documento": factura["doc_id"],
            "total": documento["totales"]["total"],
            "ts": datetime.utcnow().isoformat()
        }
    )

    return {
        "status": "OK",
        "documento": factura
    }
