# ============================================================
# integrations_connectors.py
# NEXO / ZYRA — INTEGRACIONES EXTERNAS
# CONECTORES (PLACEHOLDERS)
# PASIVO | SIN EJECUTAR LLAMADAS REALES
# ============================================================

def build_connector(integration: dict) -> dict:
    """
    Construye un descriptor de conexión.
    No ejecuta requests.
    """
    return {
        "integration_id": integration.get("integration_id"),
        "provider": integration.get("provider"),
        "service": integration.get("service"),
        "endpoint": integration.get("endpoint"),
        "method": integration.get("method", "POST"),
        "headers": integration.get("headers", {}),
        "status": "READY"
    }