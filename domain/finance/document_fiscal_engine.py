# ============================================================
# document_fiscal_engine.py
# NEXO / ZYRA — MOTOR DE DOCUMENTOS FISCALES UNIVERSAL
# Inmutable | Multipaís | Basado en Eventos | Audit-ready
# ============================================================

import os
import json
import uuid
from copy import deepcopy
from datetime import datetime

# ============================================================
# CONFIGURACIÓN BASE
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DOCS_FILE = os.path.join(DATA_DIR, "fiscal_documents.json")
SIMULATIONS_FILE = os.path.join(DATA_DIR, "fiscal_simulations.json")

os.makedirs(DATA_DIR, exist_ok=True)

for fpath in [DOCS_FILE, SIMULATIONS_FILE]:
    if not os.path.exists(fpath):
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)

# ============================================================
# UTILIDADES INTERNAS
# ============================================================

def _now():
    return datetime.utcnow().isoformat()

def _uid():
    return str(uuid.uuid4())

def _load(path, default=None):
    default = default or []
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else default
    except Exception:
        return default

def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# ============================================================
# DOCUMENTOS FISCALES REALES
# ============================================================

def add_document(doc: dict):
    """
    Guarda un documento fiscal real
    """
    doc_copy = deepcopy(doc)
    doc_copy["doc_id"] = f"DOC-{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}"
    doc_copy["ts"] = _now()
    doc_copy["estado"] = "EMITIDO"

    data = _load(DOCS_FILE)
    data.append(doc_copy)
    _save(DOCS_FILE, data)
    return doc_copy

def get_all_documents():
    return _load(DOCS_FILE)

# ============================================================
# SIMULACIONES FISCALES
# ============================================================

def add_simulation(doc: dict):
    """
    Guarda un documento simulado
    """
    doc_copy = deepcopy(doc)
    doc_copy["ts"] = _now()
    doc_copy["valido"] = True
    doc_copy["preview"] = deepcopy(doc_copy)

    data = _load(SIMULATIONS_FILE)
    data.append(doc_copy)
    _save(SIMULATIONS_FILE, data)
    return doc_copy

def get_all_simulations():
    return _load(SIMULATIONS_FILE)

# ============================================================
# API PÚBLICA CANÓNICA
# ============================================================

def simular_documento(doc: dict) -> dict:
    """
    Simula un documento fiscal y lo registra en simulaciones.
    """
    simulacion = deepcopy(doc)
    simulacion["valido"] = True
    simulacion["riesgo"] = "BAJO"
    simulacion["observaciones"] = []
    simulacion["preview"] = deepcopy(simulacion)

    if doc.get("totales", {}).get("total", 0) <= 0:
        simulacion["valido"] = False
        simulacion["riesgo"] = "ALTO"
        simulacion["observaciones"].append("Total inválido")

    add_simulation(simulacion)
    return simulacion

def generar_documento(doc: dict) -> dict:
    """
    Genera un documento fiscal real basado en la simulación o entrada.
    """
    return add_document(doc)

# ============================================================
# CONSULTAS
# ============================================================

def documentos_por_pais(pais: str):
    return [d for d in get_all_documents() if d.get("data", {}).get("pais") == pais]

def documentos_por_cliente(cliente_id: str):
    return [d for d in get_all_documents() if d.get("data", {}).get("cliente", {}).get("id") == cliente_id]

# ============================================================
# PRUEBA LOCAL
# ============================================================

if __name__ == "__main__":
    factura = {
        "pais": "SV",
        "sector": "FARMACIA",
        "tipo_documento": "FACTURA",
        "cliente": {"id": "CLI-001", "nombre": "Cliente Prueba"},
        "eventos_ref": ["POS-778"],
        "totales": {"subtotal": 10.00, "iva": 1.30, "total": 11.30, "moneda": "USD"}
    }

    print("▶ Simulación ZYRA")
    print(simular_documento(factura))

    print("▶ Emisión documento")
    print(generar_documento(factura))