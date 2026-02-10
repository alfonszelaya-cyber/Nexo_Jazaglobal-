# ============================================================
# root_controller.py
# NEXO / ZYRA — ROOT CONTROLLER (CORE PERMANENTE)
# ============================================================

import os
import importlib.util

# BASE_DIR correcto (raíz Nexo_Jazaglobal)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ---------- helpers seguros ----------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header():
    print("============================================================")
    print("                ZYRA / NEXO CORE SYSTEM                     ")
    print("============================================================")

# ledger_record seguro (si existe en core)
try:
    from core.ledger import ledger_record
except:
    def ledger_record(msg):
        print(f"[LEDGER] {msg}")

# ============================================================
# CARGADOR SEGURO
# ============================================================
def load_module(file, func):
    path = os.path.join(BASE_DIR, "module", file)  # 👈 module (no modules)
    if not os.path.exists(path):
        return None

    spec = importlib.util.spec_from_file_location(file, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    ledger_record(file.replace(".py", "") + " cargado")
    return getattr(mod, func, None)

# ============================================================
# ROOT CONTROLLER
# ============================================================
def root_controller():

    ledger_record("ROOT_CONTROLLER_STARTED")

    mod_1  = load_module("modulo_1_panel_ejecutivo.py", "modulo_1_panel_ejecutivo")
    mod_2  = load_module("modulo_2_inscripciones.py", "modulo_2_inscripciones")
    mod_3  = load_module("modulo_3_radar_vip.py", "modulo_3_radar_vip")
    mod_4  = load_module("modulo_4_finanzaas_condoble.py", "modulo_4_finanzaas_condoble")
    mod_5  = load_module("modulo_5_logistica.py", "modulo_5_logistica")
    mod_6  = load_module("modulo_6_riesgo.py", "modulo_6_riesgo")
    mod_7  = load_module("modulo_7_seguridad_identida.py", "modulo_7_seguridad_identida")
    mod_8  = load_module("modulo_8_gobierno.py", "modulo_8_gobierno")
    mod_9  = load_module("modulo_9_meta_gobierno.py", "modulo_9_meta_gobierno")
    mod_10 = load_module("modulo_10_atencion_al_cliente.py", "modulo_10_atencion_al_cliente")
    mod_001 = load_module("modulo_001_super_bunker.py", "modulo_001_super_bunker")

    while True:
        clear()
        header()
        print("""
--- NEXO / ZYRA ROOT ---
1) Status del sistema
2) Modulo 1 Panel Ejecutivo
3) Modulo 2 Inscripciones
4) Modulo 3 Radar Vip
5) Modulo 4 Finanzaas Condoble
6) Modulo 5 Logistica
7) Modulo 6 Riesgo
8) Modulo 7 Seguridad Identida
9) Modulo 8 Gobierno
10) Modulo 9 Meta Gobierno
11) Modulo 10 Atencion Al Cliente
12) Módulo 001 Super Búnker
0) Salir
""")

        cmd = input(">> ").strip()

        if cmd == "1":
            input("\nSistema OK [ENTER]")

        elif cmd == "2" and mod_1: mod_1()
        elif cmd == "3" and mod_2: mod_2()
        elif cmd == "4" and mod_3: mod_3()
        elif cmd == "5" and mod_4: mod_4()
        elif cmd == "6" and mod_5: mod_5()
        elif cmd == "7" and mod_6: mod_6()
        elif cmd == "8" and mod_7: mod_7()
        elif cmd == "9" and mod_8: mod_8()
        elif cmd == "10" and mod_9: mod_9()
        elif cmd == "11" and mod_10: mod_10()
        elif cmd == "12" and mod_001: mod_001()

        elif cmd == "0":
            ledger_record("SYSTEM_EXIT")
            break
        else:
            input("Comando inválido [ENTER]")