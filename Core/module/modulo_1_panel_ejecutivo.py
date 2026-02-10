# ============================================================
# MODULO 1 : PANEL EJECUTIVO (CALLABLE DESDE MAIN)
# ============================================================

import os

# ============================================================
# FUNCIONES DE APOYO
# ============================================================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print("============================================================")
    print("                ZYRA / NEXO CORE SYSTEM                     ")
    print("============================================================")

def pausa(titulo=""):
    if titulo:
        print(f"\n{titulo}")
    input("\n[ENTER] para continuar...")

def menu_simple(titulo, opciones):
    while True:
        clear()
        header()
        print(f"{titulo}\n")
        for i, op in enumerate(opciones, 1):
            print(f"{i}. {op}")
        print("0. Volver")
        o = input("> ")
        if o == "0":
            break
        try:
            idx = int(o) - 1
            if 0 <= idx < len(opciones):
                pausa(f"Accediendo a: {opciones[idx]}")
            else:
                pausa("Opción no válida.")
        except:
            pausa("Entrada no válida.")

# ============================================================
# MODULO 1 PANEL EJECUTIVO
# ============================================================
def modulo_1_panel_ejecutivo():
    while True:
        clear()
        header()
        print("""
ZYRA / NEXO CORE — PANEL EJECUTIVO

1. Resumen General
2. Estado Financiero
3. Estado Fiscal
4. Alertas Globales
5. KPIs Ejecutivos
6. Decisiones Estratégicas
0. Volver a ROOT
""")
        op = input("> ")
        if op == "1":
            menu_simple(
                "Resumen General",
                ["Ingresos", "Egresos", "Utilidad", "Operaciones Activas"]
            )
        elif op == "2":
            menu_simple(
                "Estado Financiero",
                ["Balance General", "Resultados", "Flujo de Caja"]
            )
        elif op == "3":
            menu_simple(
                "Estado Fiscal",
                ["Impuestos Pendientes", "Declaraciones", "Riesgos Fiscales"]
            )
        elif op == "4":
            menu_simple(
                "Alertas Globales",
                ["Riesgo Alto", "Bloqueos", "Incidentes Críticos"]
            )
        elif op == "5":
            menu_simple(
                "KPIs Ejecutivos",
                ["Rentabilidad", "Liquidez", "Rotación", "Crecimiento"]
            )
        elif op == "6":
            menu_simple(
                "Decisiones Estratégicas",
                ["Aprobar", "Revisar", "Bloquear"]
            )
        elif op == "0":
            break
        else:
            pausa("Opción inválida")