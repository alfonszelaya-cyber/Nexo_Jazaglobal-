# ============================================================
# export_engine.py
# NEXO / ZYRA — EXPORT ENGINE
# Lógica base de exportaciones
# ============================================================

def create_export(data: dict):
    return {
        "status": "CREATED",
        "export_id": data.get("export_id"),
        "origin": data.get("origin"),
        "destination": data.get("destination"),
        "cargo": data.get("cargo"),
    }


def get_export_status(export_id: str):
    return {
        "export_id": export_id,
        "status": "PENDING"
    }