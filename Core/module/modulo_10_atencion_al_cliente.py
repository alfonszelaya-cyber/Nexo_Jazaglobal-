# =====================================================
# NEXO / ZYRA
# MÓDULO 10 — ATENCIÓN AL CLIENTE & SOPORTE (LIMPIO)
# =====================================================

import os

# ===============================
# UI BÁSICA
# ===============================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPresiona ENTER para volver...")

def menu(title, options):
    while True:
        clear()
        print(f"\n=== {title} ===")
        for i, opt in enumerate(options.keys(), 1):
            print(f"{i}. {opt}")
        print("0. Volver")

        op = input("> ").strip()

        if op == "0":
            return
        if op.isdigit() and 1 <= int(op) <= len(options):
            list(options.values())[int(op) - 1]()
        else:
            print("Opción inválida")
            pause()

def hoja(nombre):
    def inner():
        clear()
        print(f"\n[{nombre}]")
        pause()
    return inner

# ===============================
# SUBMÓDULOS
# ===============================
def entrada_soporte():
    menu("Entrada de Soporte", {
        "Identificación del Cliente": hoja("Identificación del Cliente"),
        "Módulo Afectado": hoja("Módulo Afectado"),
        "Tipo de Problema": hoja("Tipo de Problema"),
        "Nivel de Urgencia": hoja("Nivel de Urgencia"),
        "Historial Automático": hoja("Historial Automático"),
    })

def atencion_automatica():
    menu("Atención Automatizada ZYRA", {
        "Diagnóstico del Problema": hoja("Diagnóstico del Problema"),
        "Resolución Automática": hoja("Resolución Automática"),
        "Respuestas Guiadas": hoja("Respuestas Guiadas"),
        "Validaciones de Estado": hoja("Validaciones de Estado"),
        "Escalamiento Automático": hoja("Escalamiento Automático"),
    })

def asesoria_operativa():
    menu("Asesoría Operativa", {
        "Qué Acción Tomar": hoja("Qué Acción Tomar"),
        "Opciones Disponibles": hoja("Opciones Disponibles"),
        "Impacto de Decisiones": hoja("Impacto de Decisiones"),
        "Advertencias de Riesgo": hoja("Advertencias de Riesgo"),
        "Confirmación Asistida": hoja("Confirmación Asistida"),
    })

def incidencias_financieras():
    menu("Incidencias Financieras", {
        "Facturas Faltantes / Erróneas": hoja("Facturas Faltantes / Erróneas"),
        "Pagos No Reflejados": hoja("Pagos No Reflejados"),
        "Transferencias en Proceso": hoja("Transferencias en Proceso"),
        "Impuestos / Retenciones": hoja("Impuestos / Retenciones"),
        "Correcciones Guiadas": hoja("Correcciones Guiadas"),
    })

def incidencias_operativas():
    menu("Incidencias Operativas", {
        "Procesos Detenidos": hoja("Procesos Detenidos"),
        "Órdenes Incompletas": hoja("Órdenes Incompletas"),
        "Estados Inconsistentes": hoja("Estados Inconsistentes"),
        "Documentación Faltante": hoja("Documentación Faltante"),
        "Corrección en Vivo": hoja("Corrección en Vivo"),
    })

def atencion_humana():
    menu("Atención Humana", {
        "Asignación de Agente": hoja("Asignación de Agente"),
        "Intervención Especializada": hoja("Intervención Especializada"),
        "Resolución Manual": hoja("Resolución Manual"),
        "Validación Final": hoja("Validación Final"),
    })

def seguimiento_casos():
    menu("Seguimiento de Casos", {
        "Casos Abiertos": hoja("Casos Abiertos"),
        "Casos en Proceso": hoja("Casos en Proceso"),
        "Casos Críticos": hoja("Casos Críticos"),
        "Historial Completo": hoja("Historial Completo"),
        "Reapertura": hoja("Reapertura"),
    })

def alertas_sla():
    menu("Alertas & SLA", {
        "Riesgo Financiero": hoja("Riesgo Financiero"),
        "Bloqueos Operativos": hoja("Bloqueos Operativos"),
        "Incidentes Críticos": hoja("Incidentes Críticos"),
        "Escalamiento Prioritario": hoja("Escalamiento Prioritario"),
    })

def cierre_caso():
    menu("Cierre del Caso", {
        "Confirmación del Cliente": hoja("Confirmación del Cliente"),
        "Evidencia Registrada": hoja("Evidencia Registrada"),
        "Nivel de Satisfacción": hoja("Nivel de Satisfacción"),
        "Cierre Definitivo": hoja("Cierre Definitivo"),
    })

def aprendizaje_zyra():
    menu("Aprendizaje ZYRA", {
        "Patrones de Fallos": hoja("Patrones de Fallos"),
        "Mejora de Respuestas": hoja("Mejora de Respuestas"),
        "Prevención Futura": hoja("Prevención Futura"),
        "Optimización Continua": hoja("Optimización Continua"),
    })

# ===============================
# ENTRADA OFICIAL PARA CORE
# ===============================
def modulo_10_atencion_al_cliente():
    menu("ATENCIÓN AL CLIENTE & SOPORTE", {
        "Entrada de Soporte": entrada_soporte,
        "Atención Automatizada ZYRA": atencion_automatica,
        "Asesoría Operativa": asesoria_operativa,
        "Incidencias Financieras": incidencias_financieras,
        "Incidencias Operativas": incidencias_operativas,
        "Atención Humana": atencion_humana,
        "Seguimiento de Casos": seguimiento_casos,
        "Alertas & SLA": alertas_sla,
        "Cierre del Caso": cierre_caso,
        "Aprendizaje ZYRA": aprendizaje_zyra,
    })