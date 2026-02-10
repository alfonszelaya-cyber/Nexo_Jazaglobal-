# ==========================================
# NEXO / ZYRA
# MÓDULO 8 — GOBIERNO DEL SISTEMA
# Menú Jerárquico Navegable en Consola
# ==========================================

def pause():
    input("\nPresiona ENTER para volver...")

def menu(title, options):
    while True:
        print(f"\n=== {title} ===")
        for i, opt in enumerate(options.keys(), start=1):
            print(f"{i}. {opt}")
        print("0. Volver")

        choice = input("> ")

        if choice == "0":
            return

        try:
            selected = list(options.values())[int(choice) - 1]
            selected()
        except:
            print("Opción inválida")

# -------------------------
# SUBMENÚS HOJA
# -------------------------
def hoja(nombre):
    def inner():
        print(f"\n[{nombre}]")
        pause()
    return inner

# -------------------------
# MENÚS DEL MÓDULO 8
# -------------------------

def nucleo_gobierno():
    menu("Núcleo de Gobierno", {
        "Estado Transversal Permanente": hoja("Estado Transversal Permanente"),
        "Supervisión Global de Módulos": hoja("Supervisión Global de Módulos"),
        "Orquestación de Estados (1–8)": hoja("Orquestación de Estados (1–8)"),
        "Verdad Única del Sistema": hoja("Verdad Única del Sistema"),
    })

def control_versiones():
    menu("Control de Versiones Avanzado", {
        "Versionado Global": hoja("Versionado Global"),
        "Versionado por Módulo": hoja("Versionado por Módulo"),
        "Versionado de Reglas ZYRA": hoja("Versionado de Reglas ZYRA"),
        "Versionado de Datos Críticos": hoja("Versionado de Datos Críticos"),
        "Firmas Criptográficas": hoja("Firmas Criptográficas"),
        "Línea de Tiempo de Versiones": hoja("Línea de Tiempo de Versiones"),
    })

def gobierno_cambios():
    menu("Gobierno de Cambios", {
        "Propuestas de Cambio": hoja("Propuestas de Cambio"),
        "Simulación Previa (Estado 7)": hoja("Simulación Previa (Estado 7)"),
        "Impacto Legal / Financiero / Operativo": hoja("Impacto Legal / Financiero / Operativo"),
        "Aprobación Escalonada": hoja("Aprobación Escalonada"),
        "Firma ROOT / Multi-Firma": hoja("Firma ROOT / Multi-Firma"),
        "Registro de Decisión": hoja("Registro de Decisión"),
    })

def auditoria_suprema():
    menu("Auditoría Suprema", {
        "Auditoría Total del Sistema": hoja("Auditoría Total del Sistema"),
        "Auditoría de Accesos": hoja("Auditoría de Accesos"),
        "Auditoría de Decisiones ZYRA": hoja("Auditoría de Decisiones ZYRA"),
        "Auditoría de Reglas": hoja("Auditoría de Reglas"),
        "Auditoría de Datos": hoja("Auditoría de Datos"),
        "Auditoría Forense": hoja("Auditoría Forense"),
        "Logs Inmutables": hoja("Logs Inmutables"),
    })

def rollback_recuperacion():
    menu("Rollback & Recuperación", {
        "Rollback por Módulo": hoja("Rollback por Módulo"),
        "Rollback Global": hoja("Rollback Global"),
        "Recuperación Post-Incidente": hoja("Recuperación Post-Incidente"),
        "Validación de Integridad": hoja("Validación de Integridad"),
        "Registro de Reversiones": hoja("Registro de Reversiones"),
    })

def gestion_incidentes():
    menu("Gestión de Incidentes Críticos", {
        "Incidentes de Seguridad": hoja("Incidentes de Seguridad"),
        "Incidentes Operativos": hoja("Incidentes Operativos"),
        "Incidentes Financieros": hoja("Incidentes Financieros"),
        "Incidentes Legales / Fiscales": hoja("Incidentes Legales / Fiscales"),
        "Clasificación de Severidad": hoja("Clasificación de Severidad"),
        "Resolución y Cierre": hoja("Resolución y Cierre"),
    })

def escalamiento_inteligente():
    menu("Escalamiento Inteligente", {
        "Escalamiento Automático ZYRA": hoja("Escalamiento Automático ZYRA"),
        "Escalamiento a Humano": hoja("Escalamiento a Humano"),
        "Escalamiento a ROOT": hoja("Escalamiento a ROOT"),
        "Umbrales Críticos": hoja("Umbrales Críticos"),
        "Notificaciones Estratégicas": hoja("Notificaciones Estratégicas"),
    })

def gobierno_zyra():
    menu("Gobierno de ZYRA", {
        "Límites de Autonomía": hoja("Límites de Autonomía"),
        "Reglas de Decisión Permitidas": hoja("Reglas de Decisión Permitidas"),
        "Decisiones Restringidas": hoja("Decisiones Restringidas"),
        "Supervisión de Aprendizaje": hoja("Supervisión de Aprendizaje"),
        "Bloqueo de IA": hoja("Bloqueo de IA"),
    })

def modo_crisis():
    menu("Modo Crisis / Emergencia", {
        "Activación Manual o Automática": hoja("Activación Manual o Automática"),
        "Congelación de Operaciones": hoja("Congelación de Operaciones"),
        "Prioridad de Seguridad": hoja("Prioridad de Seguridad"),
        "Comunicación de Estado": hoja("Comunicación de Estado"),
        "Retorno Controlado": hoja("Retorno Controlado"),
    })

def cumplimiento_soberania():
    menu("Cumplimiento & Soberanía", {
        "Cumplimiento Legal Global": hoja("Cumplimiento Legal Global"),
        "Cumplimiento por País": hoja("Cumplimiento por País"),
        "Reguladores & Auditorías Externas": hoja("Reguladores & Auditorías Externas"),
        "Evidencia Legal": hoja("Evidencia Legal"),
        "Exportación Certificada": hoja("Exportación Certificada"),
    })

def supervision_root():
    menu("Supervisión ROOT Suprema", {
        "Vista Total del Sistema": hoja("Vista Total del Sistema"),
        "Control Absoluto": hoja("Control Absoluto"),
        "Autorizaciones Máximas": hoja("Autorizaciones Máximas"),
        "Activación / Desactivación de Módulos": hoja("Activación / Desactivación de Módulos"),
        "Firma Final": hoja("Firma Final"),
    })

def congelacion_sellado():
    menu("Congelación & Sellado", {
        "Congelar Blueprint": hoja("Congelar Blueprint"),
        "Congelar Código": hoja("Congelar Código"),
        "Congelar Reglas": hoja("Congelar Reglas"),
        "Sellado de Estado": hoja("Sellado de Estado"),
        "Referencia Histórica Inmutable": hoja("Referencia Histórica Inmutable"),
    })

# -------------------------
# ENTRADA PARA CORE
# -------------------------
def modulo_8_gobierno():
    menu("MÓDULO 8 — GOBIERNO DEL SISTEMA", {
        "Núcleo de Gobierno": nucleo_gobierno,
        "Control de Versiones Avanzado": control_versiones,
        "Gobierno de Cambios": gobierno_cambios,
        "Auditoría Suprema": auditoria_suprema,
        "Rollback & Recuperación": rollback_recuperacion,
        "Gestión de Incidentes Críticos": gestion_incidentes,
        "Escalamiento Inteligente": escalamiento_inteligente,
        "Gobierno de ZYRA": gobierno_zyra,
        "Modo Crisis / Emergencia": modo_crisis,
        "Cumplimiento & Soberanía": cumplimiento_soberania,
        "Supervisión ROOT Suprema": supervision_root,
        "Congelación & Sellado": congelacion_sellado,
    })