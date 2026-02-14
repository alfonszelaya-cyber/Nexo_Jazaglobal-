# ============================================================
# ZYRA / NEXO
# SALES FLOW TEMPLATE
# VERSION 2.0 – COMMERCIAL INTELLIGENCE READY
# ============================================================

SALES_FLOW_TEMPLATE = {
    "meta": {
        "flow_id": "auto_uuid",
        "version": "2.0",
        "region": "auto",
        "country": "auto",
        "created_at_utc": "auto",
        "updated_at_utc": "auto"
    },

    "client": {
        "client_id": "",
        "legal_name": "",
        "client_type": "NATURAL",
        "segment": "STANDARD",  # STANDARD | VIP | CORPORATE
        "risk_score": 0
    },

    "commercial_data": {
        "quote_id": "",
        "status": "DRAFT",  # DRAFT | SENT | NEGOTIATING | CLOSED
        "valid_until": "auto",
        "sales_channel": "DIRECT"
    },

    "products": [],

    "logistics": {
        "delivery_type": "LAND",
        "warehouse_origin": "",
        "tracking_code": "",
        "estimated_delivery": "auto"
    },

    "financial_projection": {
        "projected_revenue": 0.0,
        "projected_margin": 0.0,
        "cost_estimate": 0.0,
        "currency": "USD"
    },

    "intelligence": {
        "recommended_price": 0.0,
        "risk_alert": False,
        "upsell_opportunities": [],
        "cross_sell_suggestions": []
    },

    "audit": {
        "history": [],
        "immutable_hash": "auto_hash"
    }
}
