# ============================================================
# export_bootstrap.py
# NEXO / ZYRA — EXPORT MODULE BOOTSTRAP
# Activa el módulo export sin tocar el MAIN
# ============================================================

def bootstrap_export():
    return {
        "module": "EXPORT",
        "status": "READY",
        "components": [
            "export_engine",
            "export_documents",
            "export_costs",
            "export_tracking",
            "export_events",
            "export_validators",
            "export_alerts",
            "export_health"
        ]
    }


# Auto-registro seguro
EXPORT_MODULE = bootstrap_export()