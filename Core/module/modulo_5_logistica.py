# ============================================================
# MODULO 5 - OPERACIONES & LOGISTICA
# ============================================================

import os

# ===============================
# UI BASE (AUTÓNOMA)
# ===============================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print("============================================================")
    print("      ZYRA / NEXO - MODULO 5 OPERACIONES & LOGISTICA        ")
    print("============================================================")

def pausa(msg=""):
    if msg:
        print(f"\n{msg}")
    input("\n[ENTER] para continuar...")

def menu_simple(titulo, opciones):
    clear()
    header()
    print(f"\n{titulo}\n")
    for i, o in enumerate(opciones, 1):
        print(f"{i}. {o}")
    pausa()

# ============================================================
# MODULO 5
# ============================================================
def modulo_5_logistica():
    while True:
        clear()
        header()
        print("""
1) Operaciones
2) Logística
3) Aduanas
4) Inventarios
5) Proveedores
6) Costos Operativos
7) Cumplimiento Operativo
8) Incidentes
9) Panel Operativo
0) Volver
""")

        op = input(">> ").strip()

        if op == "1":
            menu_simple("OPERACIONES", [
                "Órdenes Activas",
                "Órdenes Completadas",
                "Órdenes Canceladas",
                "Historial"
            ])

        elif op == "2":
            menu_simple("LOGÍSTICA", [
                "Terrestre",
                "Marítimo",
                "Aéreo",
                "Proveedores",
                "Costos"
            ])

        elif op == "3":
            menu_simple("ADUANAS", [
                "Documentación",
                "Despacho",
                "Impuestos",
                "Estados",
                "Historial"
            ])

        elif op == "4":
            menu_simple("INVENTARIOS", [
                "Entradas",
                "Salidas",
                "Stock",
                "Ubicaciones",
                "Ajustes",
                "Historial"
            ])

        elif op == "5":
            menu_simple("PROVEEDORES", [
                "Registro",
                "Evaluación",
                "Contratos",
                "Historial"
            ])

        elif op == "6":
            menu_simple("COSTOS OPERATIVOS", [
                "Directos",
                "Indirectos",
                "Por Operación",
                "Comparativos"
            ])

        elif op == "7":
            menu_simple("CUMPLIMIENTO OPERATIVO", [
                "Reglas",
                "Restricciones",
                "Validaciones",
                "Alertas"
            ])

        elif op == "8":
            menu_simple("INCIDENTES", [
                "Reportar",
                "Abiertos",
                "Cerrados",
                "Historial"
            ])

        elif op == "9":
            menu_simple("PANEL OPERATIVO", [
                "Estado General",
                "Alertas",
                "Cuellos de Botella",
                "KPIs"
            ])

        elif op == "0":
            break

        else:
            pausa("Opción inválida")