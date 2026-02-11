# ============================================================
# zyra_tur.py
# ZYRA Trusted Universal Resolver (TUR)
# Resolución confiable de país, moneda, rol y nivel
# ============================================================

import datetime
from domain.system.system_constants import SensitiveAction, ROLE_ROOT, ROLE_SYSTEM

# Base extensible (NO hardcode frágil)
_COUNTRY_CONTEXT = {
    "US": {"currency": "USD"},
    "GT": {"currency": "GTQ"},
    "MX": {"currency": "MXN"},
    "NI": {"currency": "NIO"},
    "CN": {"currency": "CNY"},
    "GLOBAL": {"currency": "USD"}
}

_ROLE_LEVELS = {
    "ROOT": 4,
    "SYSTEM": 4,
    "CORPORATION": 3,
    "MANAGER": 2,
    "USER": 1
}

# -------------------------
# FUNCIONES BASE
# -------------------------
def resolve_country(country_code: str):
    return _COUNTRY_CONTEXT.get(country_code, _COUNTRY_CONTEXT["GLOBAL"])

def resolve_currency_flow(payer_currency: str, receiver_currency: str):
    return {
        "conversion_required": payer_currency != receiver_currency,
        "from": payer_currency,
        "to": receiver_currency
    }

def resolve_access_level(role: str):
    return _ROLE_LEVELS.get(role, 1)

def tur_snapshot(context: dict):
    return {
        "context": context,
        "trusted": True,
        "schema": "1",
        "resolved_at": datetime.datetime.utcnow().isoformat()
    }

# -------------------------
# CLASE PRINCIPAL (API)
# -------------------------
class ZYRA_TUR:

    def __init__(self):
        self.engine_name = "ZYRA_TUR"
        self.version = "1.0.0"

    def authorize(self, role: str, action: SensitiveAction) -> bool:

        if role in (ROLE_ROOT, ROLE_SYSTEM):
            return True

        if action == SensitiveAction.VIEW:
            return True

        if action in (SensitiveAction.EXECUTE, SensitiveAction.MODIFY):
            return resolve_access_level(role) >= 2

        if action in (SensitiveAction.DELETE, SensitiveAction.UNLOCK):
            return False

        return False

    def resolve_context(self, role: str, country_code: str):
        country = resolve_country(country_code)
        level = resolve_access_level(role)

        return tur_snapshot({
            "role": role,
            "level": level,
            "country": country_code,
            "currency": country["currency"]
        })
