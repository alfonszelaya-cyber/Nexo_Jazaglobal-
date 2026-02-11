import json
import os
from datetime import datetime

# ==========================================
# Rutas del búnker JazaGlobal
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# ==========================================
# RADAR GLOBAL DE ALERTA
# ==========================================

def ejecutar_alerta_general():

    print("\n" + "🚨" + "═" * 50 + "🚨")
    print("       ZYRA RADAR - ALERTA GLOBAL DE SISTEMA        ")
    print("═" * 52)

    # --------------------------------------
    # 1. VIGILANCIA DE STOCK (INVENTARIO)
    # --------------------------------------
    ruta_stock = os.path.join(DATA_DIR, "inventory.json")
    print("\n📦 [ESTADO DE INVENTARIO/STOCK]")

    inventario = []

    if os.path.exists(ruta_stock):
        try:
            with open(ruta_stock, "r", encoding="utf-8") as f:
                inventario = json.load(f)

            if len(inventario) > 0:
                print(f"   ✅ Movimientos detectados: {len(inventario)} registros.")
                print("   ℹ️  STATUS: Stock estable en Laboratorio SV.")
            else:
                print("   ⚠️  ALERTA: Inventario vacío o no registrado.")

        except Exception:
            print("   ❌ Error al leer inventario.")
    else:
        print("   ⚠️  Inventario no encontrado.")

    # --------------------------------------
    # 2. VIGILANCIA FINANCIERA
    # --------------------------------------
    print("\n💰 [ALERTA DE RENTABILIDAD]")

    ingresos = 0.0
    gastos = 0.0

    archivos_ingreso = [
        "e_invoices.json",
        "ledger.json"
    ]

    archivos_gasto = [
        "tax_declarations.json",
        "inventory.json",
        "fiscal_documents.json"
    ]

    for arc in archivos_ingreso:
        ruta = os.path.join(DATA_DIR, arc)
        if os.path.exists(ruta):
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for r in data:
                        ingresos += float(r.get("monto") or r.get("monto_usd") or 0)
            except Exception:
                pass

    for arc in archivos_gasto:
        ruta = os.path.join(DATA_DIR, arc)
        if os.path.exists(ruta):
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for r in data:
                        gastos += float(r.get("monto") or r.get("monto_usd") or 0)
            except Exception:
                pass

    balance = ingresos - gastos

    if balance > 0:
        print(f"   📈 RESULTADO: GANANDO (+ $ {balance:,.2f} USD)")
        print("   ✅ STATUS: Flujo de caja saludable.")
    elif balance == 0:
        print("   🟡 RESULTADO: PUNTO DE EQUILIBRIO ($ 0.00)")
        print("   ⚠️  STATUS: Operando sin margen de utilidad.")
    else:
        print(f"   📉 RESULTADO: PERDIENDO (- $ {abs(balance):,.2f} USD)")
        print("   🚨 ALERTA CRÍTICA: Gastos superan ingresos.")

    # --------------------------------------
    # 3. SEMÁFORO GLOBAL DE SALUD
    # --------------------------------------
    print("\n🚦 [SEMÁFORO DE SALUD JAZAGLOBAL]")

    if balance > 0 and len(inventario) > 0:
        print("   🟢 GLOBAL: SISTEMA ÓPTIMO (MENSUAL/ANUAL)")
    elif balance < 0:
        print("   🔴 GLOBAL: RIESGO FINANCIERO DETECTADO")
    else:
        print("   🟡 GLOBAL: PRECAUCIÓN / DATOS INSUFICIENTES")

    print("\n" + "═" * 52)