# =========================================
# stock_alert_engine.py
# NEXO / ZYRA — ALERTAS DE INVENTARIO UNIVERSAL
# Inmutable | Event-driven | Regla pasiva
# =========================================

from inventory_engine import obtener_stock
from radar_engine import registrar_evento

# -------------------------
# REGLA CANÓNICA DE STOCK
# -------------------------
def verificar_stock(producto_id, stock_minimo, sector):
    """
    Verifica nivel de stock en cualquier sector (Farmacia, Autos, etc.)
    y emite alerta al RADAR si es necesario.
    """

    estado = obtener_stock(producto_id)
    stock = estado.get("cantidad", 0)
    bloqueado = estado.get("bloqueado", False)

    payload = {
        "producto_id": producto_id,
        "sector": sector.upper(),
        "stock": stock,
        "stock_minimo": stock_minimo,
        "bloqueado": bloqueado
    }

    # SEÑAL DE RADAR: Si el stock es igual o menor al mínimo
    if stock <= stock_minimo:
        # Se registra como nivel 3 (Riesgo/Atención) para que Zyra lo procese
        registrar_evento(
            tipo="STOCK_CRITICO",
            origen="INVENTORY_CORE",
            descripcion=f"Alerta de inventario en {sector}: {producto_id} llegó a {stock}.",
            nivel=3,
            referencia=producto_id
        )

        return {
            "status": "ALERTA",
            "nivel": "RIESGO",
            **payload
        }

    # Operación normal
    return {
        "status": "OK",
        "msg": "Stock dentro de parámetros normales",
        **payload
    }