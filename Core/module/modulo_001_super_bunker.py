# =====================================================
# NEXO / ZYRA
# MÓDULO 001 — SUPER BÚNKER GOLD
# SEGURIDAD SUPREMA · 3 CAPAS · CONSOLA PYTHON
# =====================================================

from infrastructure.events.zyra_bus import emit

# -------------------------
# UTILIDADES
# -------------------------
def pause():
    input("\nPresiona ENTER para continuar...")


def menu(title, options):
    while True:
        print(f"\n=== {title} ===")
        for i, k in enumerate(options.keys(), 1):
            print(f"{i}. {k}")
        print("0. Volver")

        op = input("> ").strip()
        if op == "0":
            return
        try:
            list(options.values())[int(op) - 1]()
        except Exception:
            print("Opción inválida")
            pause()


def accion(nombre):
    def inner():
        print(f"\n[ACCIÓN] {nombre}")
        pause()
    return inner


# =====================================================
# CAPA 3 — ACCIONES
# =====================================================

acciones_eventos_menores = {
    "Reset de Contraseña": accion("Reset de Contraseña"),
    "Verificación por Código SMS": accion("Verificación por Código SMS"),
    "Bloqueo Temporal de Sesión": accion("Bloqueo Temporal de Sesión"),
    "Registro de Evento": accion("Registro de Evento"),
}

acciones_eventos_graves = {
    "Bloqueo de Cuenta": accion("Bloqueo de Cuenta"),
    "Congelación de Fondos": accion("Congelación de Fondos"),
    "Alerta a Seguridad": accion("Alerta a Seguridad"),
    "Evidencia Forense": accion("Evidencia Forense"),
}

acciones_crisis_suprema = {
    "Aislamiento Total del Usuario": accion("Aislamiento Total del Usuario"),
    "Cierre de Canales": accion("Cierre de Canales"),
    "Alerta ROOT": accion("Alerta ROOT"),
    "Modo Crisis Global": accion("Modo Crisis Global"),
}

acciones_identidad = {
    "Validación Biométrica": accion("Validación Biométrica"),
    "Verificación Facial": accion("Verificación Facial"),
    "Revisión Manual Identidad": accion("Revisión Manual Identidad"),
}

acciones_auditoria = {
    "Auditoría de Accesos": accion("Auditoría de Accesos"),
    "Auditoría de Cambios": accion("Auditoría de Cambios"),
    "Auditoría de Decisiones": accion("Auditoría de Decisiones"),
}

# =====================================================
# CAPA 2 — SUBDOMINIOS
# =====================================================

def eventos_menores():
    emit("SB_EVENTOS_MENORES")
    menu("Eventos Menores", acciones_eventos_menores)

def eventos_graves():
    emit("SB_EVENTOS_GRAVES")
    menu("Eventos Graves", acciones_eventos_graves)

def crisis_suprema():
    emit("SB_CRISIS_SUPREMA")
    menu("Crisis Suprema", acciones_crisis_suprema)

def identidad_seguridad():
    emit("SB_IDENTIDAD")
    menu("Identidad & Verificación", acciones_identidad)

def auditoria_suprema():
    emit("SB_AUDITORIA")
    menu("Auditoría Suprema", acciones_auditoria)

# =====================================================
# CAPA 1 — DOMINIOS
# =====================================================

def dominio_riesgos():
    emit("SB_DOMINIO_RIESGOS")
    menu("Gestión de Riesgos", {
        "Eventos Menores": eventos_menores,
        "Eventos Graves": eventos_graves,
    })

def dominio_crisis():
    emit("SB_DOMINIO_CRISIS")
    menu("Gestión de Crisis", {
        "Crisis Suprema": crisis_suprema,
    })

def dominio_identidad():
    emit("SB_DOMINIO_IDENTIDAD")
    menu("Identidad & Accesos", {
        "Verificación de Identidad": identidad_seguridad,
    })

def dominio_auditoria():
    emit("SB_DOMINIO_AUDITORIA")
    menu("Auditoría & Evidencia", {
        "Auditoría Suprema": auditoria_suprema,
    })

# =====================================================
# ENTRY POINT
# =====================================================

def modulo_001_super_bunker():
    emit("SUPER_BUNKER_GOLD_ACTIVO")
    menu(
        "SUPER BÚNKER GOLD — SEGURIDAD ABSOLUTA",
        {
            "Gestión de Riesgos": dominio_riesgos,
            "Gestión de Crisis": dominio_crisis,
            "Identidad & Accesos": dominio_identidad,
            "Auditoría & Evidencia": dominio_auditoria,
        }
    )

def main():
    modulo_001_super_bunker()
