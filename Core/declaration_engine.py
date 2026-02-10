# ============================================================
# declaration_engine.py
# Motor de declaraciones del CORE ZYRA/NEXO
# ============================================================

import os
import json
import datetime

# -----------------------------
# Configuración de declaraciones
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DECLARATION_FILE = os.path.join(DATA_DIR, "declarations.json")
os.makedirs(DATA_DIR, exist_ok=True)

# Inicializar archivo si no existe
if not os.path.exists(DECLARATION_FILE):
    with open(DECLARATION_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# -----------------------------
# Funciones de declaraciones
# -----------------------------
def add_declaration(declaration: dict):
    """
    Agrega una declaración fiscal al sistema
    """
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = {"declaration": declaration, "ts": ts}

    try:
        with open(DECLARATION_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []

    data.append(record)

    try:
        with open(DECLARATION_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

def get_all_declarations():
    """
    Retorna todas las declaraciones
    """
    try:
        with open(DECLARATION_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except Exception:
        return []

def get_declarations_by_type(declaration_type: str):
    """
    Retorna todas las declaraciones de un tipo específico
    """
    all_declarations = get_all_declarations()
    return [d for d in all_declarations if d.get("declaration", {}).get("type") == declaration_type]

def get_summary():
    """
    Retorna un resumen de declaraciones
    """
    all_declarations = get_all_declarations()
    summary = {
        "total_declarations": len(all_declarations),
    }
    return summary