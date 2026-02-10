import os
from datetime import datetime

# =====================================================
# UTILIDADES BASE
# =====================================================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    print("=" * 70)
    print("ZYRA / NEXO CORE — MÓDULO 7 SEGURIDAD & IDENTIDAD")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 70)

def pausa(nombre):
    clear()
    header()
    print(f"\n📂 {nombre}")
    input("\n[ENTER] Volver")

def submenu(nombre, opciones):
    while True:
        clear()
        header()
        print(nombre + "\n")
        for i, op in enumerate(opciones, 1):
            print(f"{i}. {op}")
        print("0. Volver")
        op = input("> ")
        if op == "0":
            break
        if op.isdigit() and 1 <= int(op) <= len(opciones):
            pausa(opciones[int(op) - 1])

# =====================================================
# MÓDULO 7 — SEGURIDAD & IDENTIDAD
# =====================================================
def modulo_7_seguridad_identida():  # nombre exacto para ZYRA_MAIN
    while True:
        clear()
        header()
        print("MÓDULO 7 — SEGURIDAD & IDENTIDAD\n")
        print("1. Identidad")
        print("2. Roles & Permisos")
        print("3. Autenticación")
        print("4. Contexto & Comportamiento")
        print("5. Bóveda de Seguridad")
        print("6. Auditoría & Registros")
        print("7. ZYRA — Seguridad Inteligente")
        print("0. Volver")

        op = input("> ")

        if op == "0":
            return

        # ===============================
        # IDENTIDAD
        # ===============================
        elif op == "1":
            while True:
                clear(); header()
                print("IDENTIDAD\n")
                print("1. Identidad Persona")
                print("2. Identidad Empresa")
                print("3. Identidad Delegada")
                print("4. Relación Persona ↔ Empresa")
                print("0. Volver")
                o = input("> ")

                if o == "0": break
                elif o == "1":
                    submenu("IDENTIDAD PERSONA", [
                        "ID ZYRA Único",
                        "Documento Legal",
                        "País",
                        "Nivel de Seguridad",
                        "Estado",
                        "Historial de Identidad"
                    ])
                elif o == "2":
                    submenu("IDENTIDAD EMPRESA", [
                        "Empresa",
                        "País Fiscal",
                        "Representante Legal",
                        "Usuarios Asociados",
                        "Nivel de Riesgo",
                        "Historial Legal"
                    ])
                elif o == "3":
                    submenu("IDENTIDAD DELEGADA", [
                        "Delegación Temporal",
                        "Alcance Permitido",
                        "Expiración"
                    ])
                elif o == "4":
                    pausa("Relación Persona ↔ Empresa")

        # ===============================
        # ROLES & PERMISOS
        # ===============================
        elif op == "2":
            while True:
                clear(); header()
                print("ROLES & PERMISOS\n")
                print("1. Roles Base")
                print("2. Permisos")
                print("3. Permisos Condicionales")
                print("4. Permisos Temporales")
                print("5. Simulación de Rol")
                print("0. Volver")
                o = input("> ")

                if o == "0": break
                elif o == "1":
                    submenu("ROLES BASE", [
                        "ROOT",
                        "Dueño",
                        "Manager",
                        "Contadora",
                        "Logística",
                        "Empleado",
                        "VIP",
                        "Corporación"
                    ])
                elif o == "2":
                    submenu("PERMISOS", ["Lectura","Ejecución","Firma","Total"])
                elif o == "3":
                    submenu("PERMISOS CONDICIONALES", ["Por Monto","Por País","Por Riesgo","Por Horario"])
                elif o == "4":
                    submenu("PERMISOS TEMPORALES", ["Inicio","Expiración"])
                elif o == "5":
                    pausa("Simulación de Rol")

        # ===============================
        # AUTENTICACIÓN
        # ===============================
        elif op == "3":
            submenu("AUTENTICACIÓN", [
                "Usuario + Password",
                "OTP",
                "Dispositivo",
                "Firma Digital",
                "Biometría",
                "Autenticación Adaptativa ZYRA",
                "Step-Up Authentication",
                "Regla 4-Ojos (Doble Autorización)"
            ])

        # ===============================
        # CONTEXTO & COMPORTAMIENTO
        # ===============================
        elif op == "4":
            submenu("CONTEXTO & COMPORTAMIENTO", [
                "Ubicación",
                "Horario",
                "Dispositivo",
                "Patrón de Uso",
                "Score de Confianza",
                "Detección de Anomalías"
            ])

        # ===============================
        # BÓVEDA DE SEGURIDAD
        # ===============================
        elif op == "5":
            submenu("BÓVEDA DE SEGURIDAD", [
                "Claves",
                "Tokens API",
                "Certificados Fiscales",
                "Firmas Digitales",
                "Accesos Bancarios",
                "Accesos con Quorum",
                "Revocación Segura",
                "Logs Inmutables"
            ])

        # ===============================
        # AUDITORÍA & REGISTROS
        # ===============================
        elif op == "6":
            submenu("AUDITORÍA & REGISTROS", [
                "Registro de Accesos",
                "Registro de Acciones",
                "Registro de Firmas",
                "Línea de Tiempo Inmutable",
                "Auditoría Forense",
                "Exportación Legal"
            ])

        # ===============================
        # ZYRA SEGURIDAD
        # ===============================
        elif op == "7":
            submenu("ZYRA — SEGURIDAD INTELIGENTE", [
                "Observación Silenciosa",
                "Evaluación de Riesgo",
                "Recomendación de Seguridad",
                "Bloqueo Gradual",
                "Escalamiento a Humano"
            ])