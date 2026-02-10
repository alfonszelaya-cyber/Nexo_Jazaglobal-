# ============================================================
# NEXO / ZYRA — MÓDULO 9
# SOBERANÍA, META-GOBIERNO & CONTINUIDAD ABSOLUTA
# ENTRY LIMPIO · INYECTABLE · ESTABLE
# ============================================================

try:
    from zyra_bus import emit
except ImportError:
    def emit(evento):
        pass


# ===============================
# UTILIDADES DE MENÚ
# ===============================
def pause():
    input("\n[ENTER] para volver...")

def menu(title, options):
    while True:
        print(f"\n=== {title} ===")
        for i, opt in enumerate(options.keys(), start=1):
            print(f"{i}. {opt}")
        print("0. Volver")

        choice = input("> ")
        if choice == "0":
            return
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            list(options.values())[int(choice) - 1]()
        else:
            print("Opción inválida")


def hoja(nombre):
    def inner():
        print(f"\n[{nombre}]")
        pause()
    return inner


# ===============================
# SUBMENÚS
# ===============================
def submenu(name):
    trees = {

        "SOBERANÍA DEL SISTEMA": [
            "Independencia Operativa",
            "Aislamiento por Jurisdicción",
            "Control de Dependencias Externas",
            "Autonomía por País",
            "Modo Soberano Offline"
        ],

        "META CONTROL DE VERSIONES": [
            "Versionado Multilínea",
            "Versionado por Jurisdicción",
            "Versionado de Estados",
            "Versionado de Modelos ZYRA",
            "Línea Temporal Inmutable"
        ],

        "AUDITORÍA META-TOTAL": [
            "Auditoría de Auditorías",
            "Auditoría de Decisiones Humanas",
            "Auditoría de Decisiones ZYRA",
            "Auditoría de Crisis",
            "Registro Inmutable Global"
        ],

        "GOBIERNO DE GOBIERNOS": [
            "Reglas de Estados",
            "Reglas de Emergencia",
            "Reglas Supra-Legales",
            "Jerarquía de Autoridades",
            "Resolución de Conflictos Normativos"
        ],

        "CONTINUIDAD ABSOLUTA": [
            "Operación Continua",
            "Auto-Recuperación",
            "Redundancia Lógica",
            "Redundancia Geográfica",
            "Persistencia ZYRA"
        ],

        "META GESTIÓN DE CRISIS": [
            "Crisis Sistémica",
            "Crisis Financiera Global",
            "Crisis Legal / Estatal",
            "Crisis Tecnológica",
            "Simulación de Supervivencia"
        ],

        "ESCALAMIENTO SUPREMO": [
            "Escalamiento Autónomo ZYRA",
            "Escalamiento Consejo Humano",
            "Escalamiento ROOT Supremo",
            "Emergencia Total"
        ],

        "GOBIERNO DE LA IA": [
            "Límites de Evolución",
            "Control de Aprendizaje",
            "Autorización de Auto-Mejora",
            "Apagado Ético"
        ],

        "ÉTICA, LEY & CONFIANZA": [
            "Principios Éticos",
            "Compatibilidad Legal Global",
            "Transparencia Controlada",
            "Evidencia Moral"
        ],

        "SUPERVISIÓN SUPRA-ROOT": [
            "Vista Omnisciente",
            "Control Transversal",
            "Decisión Final",
            "Firma Suprema"
        ],

        "SELLADO DE CIVILIZACIÓN DIGITAL": [
            "Congelación Total",
            "Sellado de Estados",
            "Archivo Histórico",
            "Referencia Canónica"
        ]
    }

    options = {item: hoja(item) for item in trees.get(name, [])}
    menu(name, options)


# ===============================
# HOOKS
# ===============================
def zyra_in():
    emit("MODULO_9_ENTRADA")

def zyra_out():
    emit("MODULO_9_SALIDA")


# ===============================
# ENTRY OFICIAL PARA MAIN
# ===============================
def modulo_9_meta_gobierno():
    zyra_in()
    menu("META GOBIERNO & SOBERANÍA SUPREMA", {
        "Soberanía del Sistema": lambda: submenu("SOBERANÍA DEL SISTEMA"),
        "Meta Control de Versiones": lambda: submenu("META CONTROL DE VERSIONES"),
        "Auditoría Meta-Total": lambda: submenu("AUDITORÍA META-TOTAL"),
        "Gobierno de Gobiernos": lambda: submenu("GOBIERNO DE GOBIERNOS"),
        "Continuidad Absoluta": lambda: submenu("CONTINUIDAD ABSOLUTA"),
        "Meta Gestión de Crisis": lambda: submenu("META GESTIÓN DE CRISIS"),
        "Escalamiento Supremo": lambda: submenu("ESCALAMIENTO SUPREMO"),
        "Gobierno de la IA": lambda: submenu("GOBIERNO DE LA IA"),
        "Ética, Ley & Confianza": lambda: submenu("ÉTICA, LEY & CONFIANZA"),
        "Supervisión Supra-Root": lambda: submenu("SUPERVISIÓN SUPRA-ROOT"),
        "Sellado de Civilización Digital": lambda: submenu("SELLADO DE CIVILIZACIÓN DIGITAL"),
    })
    zyra_out()