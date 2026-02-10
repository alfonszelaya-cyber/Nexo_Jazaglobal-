# logistics_costs.py
# NEXO / ZYRA — LOGÍSTICA ASIA
# CÁLCULO DE COSTOS LOGÍSTICOS
# PASIVO | SIN EFECTOS

def calculate_logistics_costs(payload: dict) -> dict:
    """
    Calcula costos totales de logística.
    """
    flete = payload.get("flete", 0)
    seguro = payload.get("seguro", 0)
    arancel = payload.get("arancel", 0)

    total = flete + seguro + arancel

    return {
        "shipment_id": payload.get("shipment_id"),
        "costs": {
            "flete": flete,
            "seguro": seguro,
            "arancel": arancel,
            "total": total
        }
    }