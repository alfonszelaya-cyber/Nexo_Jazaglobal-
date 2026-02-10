# ============================================================
# export_costs.py
# NEXO / ZYRA — EXPORT COSTS
# ============================================================

def calculate_export_costs(export_id: str):
    return {
        "export_id": export_id,
        "freight": 0,
        "insurance": 0,
        "taxes": 0,
        "total_cost": 0
    }