import os

# ============================================================
# FUNCIONES DE APOYO (IGUALES A MODULO 1 Y 2)
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
# MODULO 3 : RADAR VIP (CALLABLE DESDE ZYRA_MAIN)
# ============================================================
def modulo_3_radar_vip():
    while True:
        clear()
        header()
        print("""
ZYRA / NEXO CORE — RADAR VIP

1. Importaciones
2. Exportaciones
3. Comercio
4. Bienes Raíces
5. Panel Radar
0. Volver a ROOT
""")

        op = input("> ")

        if op == "1":
            menu_simple(
                "Importaciones",
                ["Fuentes", "Análisis", "Costos", "Rentabilidad"]
            )

        elif op == "2":
            menu_simple(
                "Exportaciones",
                ["Mercados", "Costos", "Logística", "Rentabilidad"]
            )

        elif op == "3":
            menu_simple(
                "Comercio",
                ["Compras", "Ventas", "Margen", "Riesgo"]
            )

        elif op == "4":
            menu_simple(
                "Bienes Raíces",
                ["Adquisición", "Costos", "Retorno", "Riesgos"]
            )

        elif op == "5":
            menu_simple(
                "Panel Radar",
                ["Alertas", "Recomendaciones ZYRA", "Historial"]
            )

        elif op == "0":
            break

        else:
            pausa("Opción inválida")