# ============================================================
# dfb_core.py
# NEXO / ZYRA — DFB CORE (DOCUMENTO FISCAL BASE)
# Facturación | Tickets | Recibos | Conexión Contable
# ============================================================

import os
import json
import uuid
from datetime import datetime

# Importamos el motor contable para conectar Facturación -> Contabilidad
try:
    from accounting_engine import registrar_evento_contable
except ImportError:
    # Fallback por si se ejecuta aislado
    def registrar_evento_contable(*args, **kwargs):
        print("[MOCK] Contabilidad notificada (Simulación)")

# -----------------------------
# CONFIGURACIÓN DE RUTAS
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

DFB_FILE = os.path.join(DATA_DIR, "dfb.json")

# -----------------------------
# UTILIDADES
# -----------------------------
def _now():
    return datetime.utcnow().isoformat()

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

# -----------------------------
# LÓGICA DEL DOCUMENTO FISCAL (CORE)
# -----------------------------
def emitir_documento_fiscal(
    tipo,            # FACTURA | TICKET | RECIBO | NOTA_CREDITO
    emisor_id,       # ID de la empresa en JAZA
    receptor_data,   # Dict con datos del cliente
    items,           # Lista de productos/servicios
    impuestos,       # Dict con detalle de impuestos
    total,
    moneda="USD",
    referencia=None
):
    """
    Crea un Documento Fiscal Base (DFB) y lo registra en Contabilidad.
    """
    
    # 1. Generar ID Único Fiscal
    dfb_id = f"DFB-{uuid.uuid4().hex[:8].upper()}"
    
    # 2. Estructura del Documento
    documento = {
        "dfb_id": dfb_id,
        "tipo": tipo,
        "emisor_id": emisor_id,
        "receptor": receptor_data,
        "items": items,
        "impuestos": impuestos,
        "subtotal": total - sum(impuestos.values()),
        "total": total,
        "moneda": moneda,
        "referencia_externa": referencia,
        "estado": "EMITIDO",
        "fecha_emision": _now(),
        "firma_digital": "PENDIENTE" # Espacio para firma electrónica futura
    }

    # 3. Guardar en Repositorio de Documentos (DFB)
    dfbs = _load(DFB_FILE)
    dfbs.append(documento)
    _save(DFB_FILE, dfbs)
    print(f"[DFB] Documento {tipo} {dfb_id} creado correctamente.")

    # 4. Impactar Automáticamente en Contabilidad (Motor ZYRA)
    # Esto automatiza el proceso: Factura creada -> Asiento contable creado
    try:
        registrar_evento_contable(
            event_type=f"EMISION_{tipo}",
            data={
                "empresa_id": emisor_id,
                "pais": receptor_data.get("pais", "SV"), # Default El Salvador
                "monto": total,
                "moneda": moneda,
                "cuenta_debito": "CUENTAS_POR_COBRAR",
                "cuenta_credito": "INGRESOS_POR_VENTA",
                "ref": dfb_id
            }
        )
    except Exception as e:
        print(f"[ALERTA] El documento se creó pero falló el registro contable: {e}")

    return documento

def consultar_documento(dfb_id):
    dfbs = _load(DFB_FILE)
    for doc in dfbs:
        if doc["dfb_id"] == dfb_id:
            return doc
    return None

# -----------------------------
# PRUEBA LOCAL
# -----------------------------
if __name__ == "__main__":
    print("--- EMISIÓN DE DOCUMENTO FISCAL ---")
    
    factura = emitir_documento_fiscal(
        tipo="FACTURA",
        emisor_id="JAZA-SV",
        receptor_data={"nombre": "Cliente Ejemplo", "nit": "0614-000000-000-0", "pais": "SV"},
        items=[
            {"producto": "Licencia Software Zyra", "cantidad": 1, "precio": 1000.00},
            {"producto": "Soporte Premium", "cantidad": 1, "precio": 200.00}
        ],
        impuestos={"IVA": 156.00}, # 13% aprox de 1200
        total=1356.00,
        moneda="USD",
        referencia="ORDEN-999"
    )
    
    print("\nDocumento Final:")
    print(json.dumps(factura, indent=2))
