"""
ZYRA LOG EVENT – CANÓNICO
Evento estándar de logging del sistema.

No ejecuta lógica.
No escribe archivos.
Es el contrato oficial del LOG_EVENT.
"""

def build_log_event(
    message: str,
    level: str = "INFO",
    source: str = "SYSTEM",
    extra: dict | None = None
) -> dict:
    return {
        "event": "LOG_EVENT",
        "payload": {
            "time": None,  # lo pone el logger
            "level": level,
            "message": message,
            "source": source,
            "extra": extra or {}
        }
    }