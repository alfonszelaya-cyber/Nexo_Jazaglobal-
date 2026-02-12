# ============================================================
# universal_events.py
# NEXO / ZYRA — UNIVERSAL EVENTS CORE
# Limpieza, normalización y persistencia de eventos
# Diseñado para operación continua 10+ años
# ============================================================

import os
import json
import re
from datetime import datetime
from 
from Core.core_ledger import ledger_record
# -----------------------------
# Configuración de almacenamiento
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
EVENTS_FILE = os.path.join(DATA_DIR, "universal_events.json")
os.makedirs(DATA_DIR, exist_ok=True)

# Inicializar archivo si no existe
if not os.path.exists(EVENTS_FILE):
    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# -----------------------------
# Funciones principales
# -----------------------------

def sanitize_text(text: str) -> str:
    """
    Limpia caracteres problemáticos, guiones largos, acentos raros y emojis.
    """
    if not isinstance(text, str):
        return str(text)
    
    # Reemplazar guiones largos y comillas tipográficas
    text = text.replace("—", "-").replace("–", "-")
    text = text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    
    # Remover caracteres no imprimibles
    text = re.sub(r"[\x00-\x1f\x7f-\x9f]", "", text)
    
    # Normalizar espacios múltiples
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

def register_universal_event(event_name: str, payload: dict, source: str = "SYSTEM") -> dict:
    """
    Registra un evento universal limpio, normalizado y auditado.
    Guarda en JSON y llama a ledger.
    """
    ts = datetime.utcnow().isoformat()

    # Limpiar payload
    clean_payload = {k: sanitize_text(v) if isinstance(v, str) else v for k, v in payload.items()}

    event_record = {
        "event": sanitize_text(event_name),
        "source": sanitize_text(source),
        "payload": clean_payload,
        "ts": ts
    }

    # Guardar en JSON
    try:
        with open(EVENTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []

    data.append(event_record)

    try:
        with open(EVENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        ledger_record(
            event="UNIVERSAL_EVENT_SAVE_ERROR",
            status="ERROR",
            detail=str(e)
        )

    # Ledger record
    ledger_record(
        event=event_record["event"],
        status="RECORDED",
        detail=event_record
    )

    return event_record

def get_all_universal_events() -> list:
    """
    Retorna todos los eventos registrados.
    """
    try:
        with open(EVENTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def clear_universal_events():
    """
    Limpia todos los eventos universales (resetea JSON)
    """
    try:
        with open(EVENTS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)
    except Exception:
        ledger_record(
            event="UNIVERSAL_EVENTS_CLEAR_ERROR",
            status="ERROR",
            detail="No se pudo limpiar el archivo de eventos"
        )

# -----------------------------
# Ejemplo de prueba
# -----------------------------
if __name__ == "__main__":
    e = register_universal_event(
        "TEST_EVENT",
        {"mensaje": "Prueba con — guion largo y “comillas” raras ✨", "valor": 123},
        source="UNIT_TEST"
    )
    print(e)
    print(get_all_universal_events())
