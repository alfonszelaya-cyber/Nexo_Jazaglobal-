# ============================================================
# ledger_finanzas.py
# Motor financiero del ledger para CORE ZYRA/NEXO
# ============================================================

import os
import json
import datetime

# -----------------------------
# Configuración del ledger financiero
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LEDGER_FILE = os.path.join(DATA_DIR, "ledger_finanzas.json")

os.makedirs(DATA_DIR, exist_ok=True)

# Inicializar archivo si no existe
if not os.path.exists(LEDGER_FILE):
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)
    print(f"[LEDGER_FINANZAS] Archivo inicializado: {LEDGER_FILE}")

# -----------------------------
# Funciones financieras
# -----------------------------
def add_finance_entry(entry: dict):
    """
    Agrega una entrada financiera al ledger
    """
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry_record = {
        "entry": entry,
        "ts": ts
    }

    try:
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []

    data.append(entry_record)

    try:
        with open(LEDGER_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[LEDGER_FINANZAS] Entrada agregada: {entry}")
    except Exception as e:
        print(f"[LEDGER_FINANZAS] Error guardando ledger: {e}")

def get_financial_summary():
    """
    Devuelve un resumen financiero del ledger
    """
    try:
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except Exception:
        data = []

    ingresos = sum(e.get("entry", {}).get("ingreso", 0) for e in data)
    egresos = sum(e.get("entry", {}).get("egreso", 0) for e in data)
    saldo = ingresos - egresos

    summary = {
        "total_ingresos": ingresos,
        "total_egresos": egresos,
        "saldo": saldo,
        "entradas": len(data)
    }

    print(f"[LEDGER_FINANZAS] Resumen financiero: {summary}")
    return summary

# -----------------------------
# Función de prueba rápida
# -----------------------------
def test_finanzas():
    add_finance_entry({"ingreso": 1000, "egreso": 200, "detalle": "Prueba"})
    get_financial_summary()