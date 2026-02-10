# ============================================================
# MODULO 4 — FINANZAS & CONTABILIDAD (CORE LOGICO)
# NEXO / ZYRA — BASE CONGELADA
# ============================================================

from datetime import datetime

# ------------------------------------------------------------
# CONFIGURACIÓN GLOBAL CORE
# ------------------------------------------------------------

SYSTEM_NAME = "NEXO / ZYRA CORE"
MODULE_NAME = "FINANZAS & CONTABILIDAD"
CURRENCY_BASE = "USD"

# ------------------------------------------------------------
# DATA MOCK (LUEGO SE CONECTA A DB / EVENTOS / ZYRA)
# NO SE MODIFICA LA LOGICA
# ------------------------------------------------------------

LEDGER = [
    {"tipo": "INGRESO", "monto": 22000},
    {"tipo": "EGRESO", "monto": 12000},
    {"tipo": "EGRESO", "monto": 3500},
    {"tipo": "EGRESO", "monto": 1800},
]

# ------------------------------------------------------------
# UTILIDADES CORE
# ------------------------------------------------------------

def header():
    print("=" * 70)
    print(f"{SYSTEM_NAME} — {MODULE_NAME}")
    print("Fecha:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 70)

# ------------------------------------------------------------
# MOTOR CONTABLE
# ------------------------------------------------------------

def calcular_finanzas(ledger):
    ingresos = sum(l["monto"] for l in ledger if l["tipo"] == "INGRESO")
    egresos = sum(l["monto"] for l in ledger if l["tipo"] == "EGRESO")
    utilidad = ingresos - egresos
    return { "ingresos": ingresos, "egresos": egresos, "utilidad": utilidad }

def estado_contable(utilidad):
    if utilidad > 0:
        return "SALUDABLE"
    elif utilidad == 0:
        return "NEUTRO"
    else:
        return "RIESGO"

# ------------------------------------------------------------
# MOTOR FISCAL (BASE)
# ------------------------------------------------------------

def calcular_impuestos(utilidad):
    if utilidad <= 0:
        return 0
    return utilidad * 0.25 # regla mock, luego ZYRA decide

# ------------------------------------------------------------
# CONTROL DE RIESGO
# ------------------------------------------------------------

def evaluar_riesgo(finanzas):
    if finanzas["utilidad"] < 0:
        return "ALTO"
    if finanzas["utilidad"] < 5000:
        return "MEDIO"
    return "BAJO"

# ------------------------------------------------------------
# EJECUCIÓN CENTRAL DEL CORE
# ------------------------------------------------------------

def ejecutar_core_finanzas():
    header()
    
    finanzas = calcular_finanzas(LEDGER)
    estado = estado_contable(finanzas["utilidad"])
    impuestos = calcular_impuestos(finanzas["utilidad"])
    riesgo = evaluar_riesgo(finanzas)

    print("\n--- RESUMEN CORE FINANCIERO ---")
    print("Ingresos Totales :", finanzas["ingresos"], CURRENCY_BASE)
    print("Egresos Totales  :", finanzas["egresos"], CURRENCY_BASE)
    print("Utilidad Neta    :", finanzas["utilidad"], CURRENCY_BASE)
    print("Estado Contable  :", estado)
    print("Impuestos Est.   :", impuestos, CURRENCY_BASE)
    print("Nivel de Riesgo  :", riesgo)
    print("\n[CORE STATUS] FINANZAS & CONTABILIDAD OK")

# ------------------------------------------------------------
# ENTRY POINT (LLAMADO DESDE ZYRA_MAIN)
# ------------------------------------------------------------

def modulo_4_core():
    ejecutar_core_finanzas()

# Si quieres probarlo directo, descomenta la linea de abajo:
if __name__ == "__main__":
    modulo_4_core()
