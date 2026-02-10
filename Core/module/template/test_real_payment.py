import os, sys, copy
from datetime import datetime, timezone

# ============================================================
# INYECTAR RUTA REAL
# core/module/template → core/module → core
# ============================================================
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODULE_DIR = os.path.dirname(CURRENT_DIR)
CORE_DIR = os.path.dirname(MODULE_DIR)

if CORE_DIR not in sys.path:
    sys.path.insert(0, CORE_DIR)

# ============================================================
# IMPORTS DEL SISTEMA REAL
# ============================================================
from payment_flow_template import PAYMENT_FLOW_TEMPLATE
from event_router import route_event
from template_validator import validate_template_instance
from template_persistence import persist_template_instance

# ============================================================
# PRUEBA REAL DE FLUJO DE PAGO
# ============================================================
def prueba_real_pago():

    pago = copy.deepcopy(PAYMENT_FLOW_TEMPLATE)

    pago["flow_metadata"]["flow_id"] = "PAGO-REAL-001"
    pago["flow_metadata"]["created_at"] = datetime.now(timezone.utc).isoformat()
    pago["flow_metadata"]["status"] = "COMPLETED"

    pago["payer"]["name"] = "Cliente VIP"
    pago["payer"]["tax_id"] = "GT-9988"

    pago["receiver"]["name"] = "Empresa JAZA"
    pago["receiver"]["tax_id"] = "GT-1122"

    pago["payment_items"][0]["reference_id"] = "FAC-001"
    pago["payment_items"][0]["description"] = "Pago Factura Enero"
    pago["payment_items"][0]["amount"] = 230
    pago["payment_items"][0]["total"] = 230
    pago["payment_items"][0]["status"] = "COMPLETED"

    pago["totals"]["subtotal"] = 230
    pago["totals"]["tax_total"] = 0
    pago["totals"]["grand_total"] = 230

    print("✅ PLANTILLA PAGO ACTIVADA:")
    print(pago)

    # ================= VALIDAR =================
    validation = validate_template_instance(pago)
    if not validation["valid"]:
        print("❌ PLANTILLA INVÁLIDA:", validation)
        return

    # ================= CORE ====================
    core_result = route_event("PAGO", pago, source="APP_REAL")

    print("\n🚀 EVENTO ENVIADO AL CORE:")
    print(core_result)

    # ================= PERSISTENCIA ============
    save_result = persist_template_instance(
        template_name="PAYMENT_FLOW_TEMPLATE",
        instance=pago,
        core_result=core_result
    )

    print("\n💾 GUARDADO EN MEMORIA:")
    print(save_result)

# ============================================================
# MAIN REAL
# ============================================================
if __name__ == "__main__":
    prueba_real_pago()