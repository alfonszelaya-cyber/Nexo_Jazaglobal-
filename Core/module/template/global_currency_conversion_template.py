# ============================================================
# ZYRA / NEXO
# PLANTILLA GLOBAL DE CONVERSIÓN MONETARIA
# CANÓNICA – 10 AÑOS
# ============================================================

GLOBAL_CURRENCY_CONVERSION_TEMPLATE = {

    "base_currencies": {
        "primary": "USD",
        "secondary": "BTC",
        "support_multi_base": True           # permite futuro EUR, CNY, etc
    },

    "client_preferences": {
        "display_currency": "client_choice",   # client_choice | country_default
        "payment_currency": "client_choice",
        "allow_multi_currency_invoice": True,
        "lock_rate_on_invoice": True            # congela tasa al emitir doc
    },

    "exchange_rate_policy": {
        "rate_source": {
            "fiat": "official_bank",            # official_bank | market | manual
            "crypto": "trusted_exchange"        # binance | coinbase | internal
        },
        "rate_update_mode": "real_time",        # real_time | interval | manual
        "update_interval_minutes": 15,
        "fallback_policy": "last_valid_rate"
    },

    "conversion_rules": {
        "conversion_path": "via_base",          # via_base | direct
        "precision": {
            "fiat_decimals": 2,
            "crypto_decimals": 8
        },
        "rounding": {
            "method": "standard",
            "bias": "neutral"                   # neutral | favor_company | favor_client
        }
    },

    "risk_controls": {
        "max_rate_variation_percent": 5,
        "alert_on_volatility": True,
        "block_on_extreme_fluctuation": True,
        "require_manual_approval_if_exceeded": True
    },

    "accounting_rules": {
        "fx_gain_loss_tracking": True,
        "post_to_account": "FX_DIFFERENCE",
        "separate_crypto_ledger": True
    },

    "compliance": {
        "respect_country_controls": True,
        "log_all_conversions": True,
        "retain_history_years": 10
    },

    "zyra_controls": {
        "auto_select_best_rate": True,
        "simulate_before_commit": True,
        "explain_conversion_to_user": True,
        "allow_future_assets": True             # oro, stablecoins, etc
    }
}

# ============================================================
# FIN DE PLANTILLA
# ============================================================