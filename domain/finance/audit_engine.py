# =========================================
# audit_engine.py
# NEXO / ZYRA — MOTOR DE AUDITORÍA AUTOMÁTICA
# Inmutable | Multipaís | Contador / Hacienda
# =========================================

from datetime import datetime
import json
import os

from infrastructure.evenst.zyra_bus import emit
from Core.core_ledger. import ledger_record
from infrastructure.logging.zyra_logs_hook import log

# -------------------------
# RUTAS BASE
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

DOCS_FILE = os.path.join(DATA_DIR, "fiscal_documents.json")
DECL_FILE = os.path.join(DATA_DIR, "tax_declarations.json")
AUDIT_FILE = os.path.join(DATA_DIR, "audit_reports.json")

# -------------------------
# UTILIDADES SEGURAS
# -------------------------
def _load(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def _now():
    return datetime.utcnow().isoformat()

# -------------------------
# AUDITORÍA CANÓNICA ZYRA
# -------------------------
def auditar_declaracion(index=-1):
    declaraciones = _load(DECL_FILE)
    documentos = _load(DOCS_FILE)

    if not declaraciones:
        log("WARN", "No hay declaraciones para auditar", "AUDIT_ENGINE")
        return {"error": "NO_DECLARACIONES"}

    decl = declaraciones[index]
    errores = []
    advertencias = []

    ref_docs = [
        d for d in documentos
        if d.get("doc_id") in decl.get("documentos", [])
    ]

    suma_docs = sum(
        d.get("data", {}).get("totales", {}).get("total", 0)
        for d in ref_docs
    )

    total_decl = decl.get("total", 0)

    if round(suma_docs, 2) != round(total_decl, 2):
        errores.append("DESCUADRE_DOCUMENTOS")

    if total_decl <= 0:
        errores.append("TOTAL_INVALIDO")

    if not ref_docs:
        errores.append("SIN_DOCUMENTOS")

    estado = "APROBADA_ZYRA"
    if errores:
        estado = "ERROR"
    elif advertencias:
        estado = "OBSERVADA"

    reporte = {
        "pais": decl.get("pais"),
        "periodo": decl.get("periodo"),
        "year": decl.get("year"),
        "month": decl.get("month"),
        "estado": estado,
        "errores": errores,
        "advertencias": advertencias,
        "timestamp": _now()
    }

    audits = _load(AUDIT_FILE)
    audits.append(reporte)
    _save(AUDIT_FILE, audits)

    emit(
        "AUDIT_COMPLETED",
        source="AUDIT_ENGINE",
        payload={"estado": estado}
    )

    ledger_record(
        event="AUDIT_COMPLETED",
        status=estado,
        detail=reporte
    )

    log("INFO", f"Auditoría finalizada: {estado}", "AUDIT_ENGINE")
    return reporte
