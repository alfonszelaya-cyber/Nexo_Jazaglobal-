# ==================================================
# MÓDULO 6 - CONTROL DE RIESGOS (CORE CALLABLE)
# ==================================================

import os

# ===============================
# UI BASE
# ===============================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    print("============================================================")
    print("        ZYRA / NEXO - MÓDULO 6 CONTROL DE RIESGOS            ")
    print("============================================================")

def pausa(msg=""):
    if msg:
        print(f"\n{msg}")
    input("\n[ENTER] para continuar...")

# ===============================
# RIESGO FINANCIERO
# ===============================
def riesgo_financiero():
    while True:
        clear()
        header()
        print("--- Riesgo Financiero ---")
        print("1) Liquidez")
        print("2) Flujo de Caja")
        print("3) Endeudamiento")
        print("4) Exposición Crediticia")
        print("5) Historial Financiero")
        print("0) Volver")
        op = input(">> ").strip()

        if op in ["1", "2", "3", "4", "5"]:
            clear()
            header()
            print("Información disponible.")
            pausa()
        elif op == "0":
            return

# ===============================
# RIESGO OPERATIVO
# ===============================
def riesgo_operativo():
    while True:
        clear()
        header()
        print("--- Riesgo Operativo ---")
        print("1) Procesos Críticos")
        print("2) Incidencias")
        print("3) Dependencias")
        print("4) Continuidad del Negocio")
        print("0) Volver")
        op = input(">> ").strip()

        if op in ["1", "2", "3", "4"]:
            clear()
            header()
            print("Información disponible.")
            pausa()
        elif op == "0":
            return

# ===============================
# OTROS RIESGOS
# ===============================
def riesgo_legal():
    clear()
    header()
    print("Riesgo Legal & Fiscal")
    print("Información disponible.")
    pausa()

def riesgo_logistico():
    clear()
    header()
    print("Riesgo Logístico")
    print("Información disponible.")
    pausa()

def riesgo_reputacional():
    clear()
    header()
    print("Riesgo Reputacional")
    print("Información disponible.")
    pausa()

def alertas_eventos():
    clear()
    header()
    print("Alertas & Eventos")
    print("Sin datos cargados.")
    pausa()

def evaluaciones_riesgo():
    clear()
    header()
    print("Evaluaciones de Riesgo")
    print("Evaluaciones pendientes.")
    pausa()

def historial_incidentes():
    clear()
    header()
    print("Historial de Incidentes")
    print("Sin registros.")
    pausa()

def panel_kpis():
    clear()
    header()
    print("Panel de Riesgos (KPIs)")
    print("Datos no cargados.")
    pausa()

# ===============================
# ENTRY ÚNICO PARA MAIN
# ===============================
def modulo_6_riesgo():
    while True:
        clear()
        header()
        print("""
1) Riesgo Financiero
2) Riesgo Operativo
3) Riesgo Legal & Fiscal
4) Riesgo Logístico
5) Riesgo Reputacional
6) Alertas & Eventos
7) Evaluaciones de Riesgo
8) Historial de Incidentes
9) Panel de Riesgos (KPIs)
0) Volver al CORE
""")
        op = input("Selecciona opción: ").strip()

        if op == "1":
            riesgo_financiero()
        elif op == "2":
            riesgo_operativo()
        elif op == "3":
            riesgo_legal()
        elif op == "4":
            riesgo_logistico()
        elif op == "5":
            riesgo_reputacional()
        elif op == "6":
            alertas_eventos()
        elif op == "7":
            evaluaciones_riesgo()
        elif op == "8":
            historial_incidentes()
        elif op == "9":
            panel_kpis()
        elif op == "0":
            return
        else:
            pausa("Opción inválida")