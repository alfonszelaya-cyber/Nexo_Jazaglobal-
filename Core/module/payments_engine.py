# ============================================================
# payments_engine.py
# NEXO / ZYRA — PAGOS & BANCOS
# MOTOR DE PAGOS
# PASIVO | EVENT-DRIVEN | ENTERPRISE READY
# ============================================================

from datetime import datetime, timezone
import uuid

# ============================================================
# UTILIDAD TIEMPO
# ============================================================

def _now():
    return datetime.now(timezone.utc).isoformat()

# ============================================================
# CREATE PAYMENT BASE (NO TOCAR)
# ============================================================

def create_payment(payload: dict) -> dict:
    """
    Crea un pago base (sin persistir).
    """
    return {
        "payment_id": payload.get("payment_id"),
        "source": payload.get("source"),          # cash / bank / gateway
        "reference": payload.get("reference"),    # sale_id / invoice_id
        "amount": payload.get("amount", 0),
        "currency": payload.get("currency", "USD"),
        "method": payload.get("method"),          # card / transfer / cash
        "status": "INITIATED",
        "ts": _now()
    }

# ============================================================
# REGISTER PAYMENT IN CORE (LO QUE PIDE EL ROUTER)
# ============================================================

def register_payment(payload: dict) -> dict:
    """
    Registro oficial del pago en CORE.
    """

    payment_id = payload.get("payment_id") or str(uuid.uuid4())

    return {
        "payment_id": payment_id,
        "payer_id": payload.get("payer_id"),
        "receiver_id": payload.get("receiver_id"),
        "amount": payload.get("amount"),
        "currency": payload.get("currency", "USD"),
        "method": payload.get("method"),
        "reference": payload.get("reference"),
        "status": "PENDING",
        "created_at": _now(),
        "history": [
            {
                "status": "PENDING",
                "timestamp": _now()
            }
        ]
    }

# ============================================================
# CONFIRM PAYMENT
# ============================================================

def confirm_payment(payment_id: str) -> dict:
    return {
        "payment_id": payment_id,
        "status": "COMPLETED",
        "confirmed_at": _now()
    }

# ============================================================
# UPDATE PAYMENT STATUS
# ============================================================

def update_payment_status(payment_id: str, new_status: str) -> dict:
    return {
        "payment_id": payment_id,
        "new_status": new_status,
        "updated_at": _now()
    }

# ============================================================
# GET PAYMENT STATUS
# ============================================================

def get_payment_status(payment_id: str) -> dict:
    return {
        "payment_id": payment_id,
        "status": "PENDING",
        "checked_at": _now()
    }
