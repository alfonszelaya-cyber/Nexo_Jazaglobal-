# ============================================================
# MODULO 2 — INSCRIPCIONES (CLIENTES & EMPRESAS)
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
# MÓDULO 2 — INSCRIPCIONES
# ============================================================
def modulo_2_inscripciones():

    # mock de contexto (luego lo dará el CORE)
    vista = "INTERNA"  # CLIENTE | INTERNA

    while True:
        clear()
        header()

        print(f"""
ZYRA / NEXO CORE — INSCRIPCIONES
VISTA ACTUAL: {vista}

1. Clientes
2. Empresas
3. Perfiles
4. Estado / Riesgo
5. Historial
0. Volver a ROOT
""")

        op = input("> ").strip()

        # -------------------------
        # CLIENTES
        # -------------------------
        if op == "1":
            if vista == "CLIENTE":
                menu_simple(
                    "Cliente – Vista Cliente",
                    ["Ver Estado", "Actualizar Datos"]
                )
            else:
                menu_simple(
                    "Clientes – Vista Interna",
                    ["Alta Cliente", "Editar Cliente", "Cambiar Estado"]
                )

        # -------------------------
        # EMPRESAS
        # -------------------------
        elif op == "2":
            if vista == "CLIENTE":
                menu_simple(
                    "Empresa – Vista Cliente",
                    ["Ver Estado", "Actualizar Datos"]
                )
            else:
                menu_simple(
                    "Empresas – Vista Interna",
                    ["Alta Empresa", "Editar Empresa", "Cambiar Estado"]
                )

        # -------------------------
        # PERFILES
        # -------------------------
        elif op == "3":
            if vista == "CLIENTE":
                menu_simple(
                    "Perfil",
                    ["Ver Rol Asignado"]
                )
            else:
                menu_simple(
                    "Perfiles – Interno",
                    ["Asignar Rol", "Cambiar Rol"]
                )

        # -------------------------
        # ESTADO / RIESGO
        # -------------------------
        elif op == "4":
            if vista == "CLIENTE":
                menu_simple(
                    "Estado del Registro",
                    ["Activo", "Pendiente", "Bloqueado"]
                )
            else:
                menu_simple(
                    "Estado / Riesgo – Interno",
                    ["Marcar Pendiente", "Aprobar", "Bloquear"]
                )

        # -------------------------
        # HISTORIAL
        # -------------------------
        elif op == "5":
            menu_simple(
                "Historial",
                ["Operaciones", "Alertas", "Auditoría"]
            )

        # -------------------------
        # SALIR
        # -------------------------
        elif op == "0":
            break

        else:
            pausa("Opción inválida")