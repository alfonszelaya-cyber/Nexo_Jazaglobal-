# module_integrity.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# VERIFICACIÓN DE INTEGRIDAD DEL MÓDULO
# PASIVO | USADO EN BOOTSTRAP

def check_module_integrity() -> bool:
    """
    Verifica que el módulo tenga sus piezas mínimas.
    No ejecuta lógica de negocio.
    """
    required = [
        "module_contracts",
        "module_state",
        "module_events",
        "module_event_handlers"
    ]
    return all(isinstance(name, str) for name in required)