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
from sales_flow_template import SALES_FLOW_TEMPLATE
from event_router import route_event
from template_validator import validate_template_instance
from template_persistence import persist_template_instance

# ============================================================
# PRUEBA REAL DE FLUJO DE VENTA
# ============================================================
def prueba_real_venta():

    venta = copy.deepcopy(SALES_FLOW_TEMPLATE)

    venta["flow_metadata"]["flow_id"] = "VENTA-REAL-001"
    venta["flow_metadata"]["created_at"] = datetime.now(timezone.utc).isoformat()
    venta["flow_metadata"]["status"] = "ACTIVE"

    venta["seller"]["name"] = "Empresa JAZA"
    venta["seller"]["tax_id"] = "GT-1122"

    venta["buyer"]["name"] = "Cliente VIP"
    venta["buyer"]["tax_id"] = "GT-9988"

    venta["products"][0]["sku"] = "SKU-001"
    venta["products"][0]["description"] = "Servicio Premium"
    venta["products"][0]["quantity"] = 2
    venta["products"][0]["unit_price"] = 100

    venta["financials"]["subtotal"] = 200
    venta["financials"]["tax_total"] = 30
    venta["financials"]["grand_total"] = 230

    print("✅ PLANTILLA ACTIVADA:")
    print(venta)

    # ================= VALIDAR =================
    validation = validate_template_instance(venta)
    if not validation["valid"]:
        print("❌ PLANTILLA INVÁLIDA:", validation)
        return

    # ================= CORE ====================
    core_result = route_event("VENTA", venta, source="APP_REAL")

    print("\n🚀 EVENTO ENVIADO AL CORE:")
    print(core_result)

    # ================= PERSISTENCIA ============
    save_result = persist_template_instance(
        template_name="SALES_FLOW_TEMPLATE",
        instance=venta,
        core_result=core_result
    )

    print("\n💾 GUARDADO EN MEMORIA:")
    print(save_result)

# ============================================================
# MAIN REAL
# ============================================================
if __name__ == "__main__":
    prueba_real_venta()