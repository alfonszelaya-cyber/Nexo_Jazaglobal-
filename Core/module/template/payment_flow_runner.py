import os
import sys
import copy
from datetime import datetime, timezone

# ============================================================
# INYECTAR RUTA REAL DEL CORE
# ============================================================
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODULE_DIR = os.path.dirname(CURRENT_DIR)   # Core/module
CORE_DIR = os.path.dirname(MODULE_DIR)      # Core

if CORE_DIR not in sys.path:
    sys.path.insert(0, CORE_DIR)

# ============================================================
# IMPORTS CANÓNICOS DEL SISTEMA
# ============================================================
from Core.module.template.payment_flow_template import PAYMENT_FLOW_TEMPLATE
from infrastructur.event.event_router import route_event

# ============================================================
# FLUJO REAL DE PAGO (LISTO PARA PRODUCCIÓN)
# ============================================================
def ejecutar_flujo_pago(payer: dict, receiver: dict, referencia: str, monto: float):
    pago = copy.deepcopy(PAYMENT_FLOW_TEMPLATE)

    pago["flow_metadata"]["flow_id"] = referencia
    pago["flow_metadata"]["created_at"] = datetime.now(timezone.utc).isoformat()
    pago["flow_metadata"]["status"] = "COMPLETED"

    pago["payer"].update(payer)
    pago["receiver"].update(receiver)

    pago["payment_items"][0]["reference_id"] = referencia
    pago["payment_items"][0]["description"] = "Pago registrado por ZYRA"
    pago["payment_items"][0]["amount"] = monto
    pago["payment_items"][0]["total"] = monto
    pago["payment_items"][0]["status"] = "COMPLETED"

    pago["totals"]["subtotal"] = monto
    pago["totals"]["grand_total"] = monto

    # ========================================================
    # EMITIR EVENTO REAL AL CORE
    # ========================================================
    resultado = route_event("PAGO", pago, source="PAYMENT_ENGINE")

    return {
        "flow": pago,
        "core_result": resultado
    }
