import os
from datetime import datetime

# ============================================================
# FUNCIONES DE APOYO (ESTÁNDAR NEXO)
# ============================================================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print("============================================================")
    print("              ZYRA / NEXO CORE SYSTEM                       ")
    print("        MODULO 4 — FINANZAAS CORE (NUCLEO CENTRAL)          ")
    print("============================================================")
    print("Fecha:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
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
        o = input("> ").strip()
        if o == "0":
            break
        try:
            idx = int(o) - 1
            if 0 <= idx < len(opciones):
                pausa(f"Accediendo a: {opciones[idx]}")
            else:
                pausa("Opción no válida")
        except:
            pausa("Entrada no válida")

# ============================================================
# DATOS SIMULADOS (MOCK — CORE REAL LOS INYECTA)
# ============================================================
SIM_LEDGER = [
    {"tipo": "INGRESO", "monto": 22000},
    {"tipo": "EGRESO", "monto": 12000},
    {"tipo": "EGRESO", "monto": 3500},
    {"tipo": "EGRESO", "monto": 1800},
]

# ============================================================
# FUNCIONES FINANCIERAS BÁSICAS
# ============================================================
def calcular_finanzas(ledger):
    ingresos = sum(l["monto"] for l in ledger if l["tipo"] == "INGRESO")
    egresos = sum(l["monto"] for l in ledger if l["tipo"] == "EGRESO")
    utilidad = ingresos - egresos
    return ingresos, egresos, utilidad

def estado_contable(utilidad):
    if utilidad > 0:
        return "SALUDABLE"
    if utilidad == 0:
        return "NEUTRO"
    return "RIESGO"

# ============================================================
# MODULO 4 — FINANZAAS CORE (NUCLEO CENTRAL)
# ============================================================
def modulo_4_finanzaas_condoble():
    while True:
        clear()
        header()
        print("""
1. Motor de Eventos
2. Contabilidad Automática
3. Motor Fiscal
4. Facturación
5. Tesorería
6. Cumplimiento Legal
7. Entregables Oficiales
8. Firmas
9. Control de Riesgo
10. Auditoría
11. Panel Financiero
0. Volver a ROOT
""")
        op = input("> ").strip()

        if op == "1":
            menu_simple(
                "Motor de Eventos",
                ["Venta", "Compra", "Importación", "Exportación", "Pago", "Cobro", "Ajuste / Cancelación"]
            )

        elif op == "2":
            menu_simple(
                "Contabilidad Automática",
                ["Asientos", "Libros", "Conciliaciones", "Historial"]
            )

        elif op == "3":
            menu_simple(
                "Motor Fiscal",
                ["Reglas", "Impuestos", "Calendario", "Simulación", "Historial"]
            )

        elif op == "4":
            menu_simple(
                "Facturación",
                ["Factura Venta", "Factura Compra", "Notas Crédito/Débito", "Historial"]
            )

        elif op == "5":
            menu_simple(
                "Tesorería",
                ["Cuentas", "Caja", "Cripto", "CxC / CxP", "Flujo"]
            )

        elif op == "6":
            menu_simple(
                "Cumplimiento Legal",
                ["Normativas", "Restricciones", "Validaciones", "Alertas"]
            )

        elif op == "7":
            menu_simple(
                "Entregables Oficiales",
                ["Gobierno", "Bancos", "Auditoría", "Cliente"]
            )

        elif op == "8":
            menu_simple(
                "Firmas",
                ["ZYRA", "Contador", "Legal", "Registro"]
            )

        elif op == "9":
            menu_simple(
                "Control de Riesgo",
                ["Fiscal", "Contable", "Liquidez", "Bloqueos"]
            )

        elif op == "10":
            menu_simple(
                "Auditoría",
                ["Interna", "Externa", "Fiscal", "Historial"]
            )

        elif op == "11":
            clear()
            header()
            ingresos, egresos, utilidad = calcular_finanzas(SIM_LEDGER)
            estado = estado_contable(utilidad)

            print("\n--- PANEL FINANCIERO ---")
            print("Ingresos Totales :", ingresos)
            print("Egresos Totales  :", egresos)
            print("Utilidad Neta    :", utilidad)
            print("Estado Contable  :", estado)
            pausa()

        elif op == "0":
            break

        else:
            pausa("Opción inválida")

# ============================================================
# MAIN (SOLO PARA PROBARLO SOLO)
# ============================================================
def main():
    modulo_4_finanzaas_condoble()

if __name__ == "__main__":
    main()