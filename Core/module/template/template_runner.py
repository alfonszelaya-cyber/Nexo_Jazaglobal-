# ============================================================
# ZYRA / NEXO — TEMPLATE RUNNER UNIVERSAL
# Ejecuta cualquier plantilla canónica del sistema
# 10+ AÑOS | PRO | INMUTABLE
# ============================================================

import os
import sys
import copy
from datetime import datetime, timezone

# ============================================================
# INYECTAR RUTA REAL DEL CORE
# ============================================================
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))      # runner/
MODULE_DIR = os.path.dirname(CURRENT_DIR)                    # module/
CORE_DIR = os.path.dirname(MODULE_DIR)                       # core/

if CORE_DIR not in sys.path:
    sys.path.insert(0, CORE_DIR)

# ============================================================
# IMPORTS DEL CORE
# ============================================================
from infrastructura.event_router import route_event

# ============================================================
# UTILIDADES
# ============================================================

def _now():
    return datetime.now(timezone.utc).isoformat()


def deep_update(target: dict, source: dict):
    """
    Inyecta datos en una plantilla sin romper estructura.
    """
    for k, v in source.items():
        if isinstance(v, dict) and isinstance(target.get(k), dict):
            deep_update(target[k], v)
        else:
            target[k] = v


def validate_template(flow: dict):
    """
    Validación mínima estructural.
    (Aquí luego puedes meter payload_validator)
    """
    if not isinstance(flow, dict):
        raise ValueError("FLOW inválido (no es dict)")

    if "flow_metadata" in flow:
        flow["flow_metadata"]["updated_at"] = _now()

    if "document_metadata" in flow:
        flow["document_metadata"]["issue_datetime"] = _now()

    return True


# ============================================================
# RUNNER PRINCIPAL
# ============================================================

def run_template(
    template: dict,
    data: dict,
    event_type: str,
    source: str = "TEMPLATE_RUNNER",
    country: str = "GLOBAL"
):
    """
    Ejecuta cualquier plantilla del sistema:
    - clona
    - inyecta datos
    - valida
    - envía al CORE
    """

    # 1. Clonar plantilla
    flow = copy.deepcopy(template)

    # 2. Inyectar datos reales
    deep_update(flow, data)

    # 3. Validar estructura
    validate_template(flow)

    # 4. Enviar evento al CORE
    result = route_event(
        event_type=event_type,
        payload=flow,
        source=source,
        country=country
    )

    return {
        "status": "OK",
        "event_result": result,
        "flow": flow
    }


# ============================================================
# NOTAS DE DISEÑO (NO TOCAR)
# ============================================================
# - Las plantillas NO tienen main
# - Este runner sirve para TODAS
# - No depende de módulos específicos
# - Compatible con 10+ años
# - Auditoría y ledger viven en event_router
# ============================================================
