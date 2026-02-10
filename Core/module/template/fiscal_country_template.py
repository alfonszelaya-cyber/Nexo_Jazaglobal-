# ============================================================
# ZYRA / NEXO
# PLANTILLA FISCAL POR PAÍS (CANÓNICA – 10+ AÑOS)
# No ejecuta lógica | Solo define estructura
# ============================================================

FISCAL_COUNTRY_TEMPLATE = {
    "country_meta": {
        "country_code": "SV",              # ISO 3166-1
        "country_name": "El Salvador",
        "region": "LATAM",
        "timezone": "America/El_Salvador",
        "languages": ["es"],
        "currency_base": "USD",
        "crypto_legal": True,
        "last_law_update": "auto"
    },

    "currency_rules": {
        "primary": "USD",
        "secondary_allowed": ["BTC"],
        "local_display": True,
        "exchange_mode": "real_time",      # real_time | daily_close | manual
        "rounding": {
            "decimals": 2,
            "method": "standard"           # standard | ceil | floor
        }
    },

    "tax_structure": {
        "vat": {
            "name": "IVA",
            "rate": 0.13,
            "applies_to": ["goods", "services"],
            "included_in_price": False
        },

        "income_tax": {
            "corporate": {
                "rate": 0.30,
                "progressive": False
            },
            "individual": {
                "progressive": True,
                "brackets": [
                    {"from": 0, "to": 4720, "rate": 0.0},
                    {"from": 4720, "to": 8950, "rate": 0.10},
                    {"from": 8950, "to": 20322, "rate": 0.20},
                    {"from": 20322, "to": None, "rate": 0.30}
                ]
            }
        },

        "customs_duties": {
            "enabled": True,
            "default_rate": "auto",
            "depends_on": ["product_type", "origin_country"]
        }
    },

    "fiscal_calendar": {
        "fiscal_year_start": "01-01",
        "fiscal_year_end": "31-12",
        "tax_filing_frequency": {
            "vat": "monthly",
            "income_tax": "annual"
        }
    },

    "documents_required": {
        "invoice": True,
        "credit_note": True,
        "debit_note": True,
        "withholding_certificate": True,
        "customs_declaration": True
    },

    "compliance_flags": {
        "electronic_invoicing": True,
        "government_api_required": False,
        "audit_retention_years": 7,
        "mandatory_digital_signature": False
    },

    "zyra_controls": {
        "auto_validate_rules": True,
        "risk_monitoring": True,
        "alert_on_law_change": True,
        "versioning_enabled": True,
        "allow_future_extension": True
    },

    "audit_trail": {
        "enabled": True,
        "immutable": True,
        "hash": "auto"
    }
}

# ============================================================
# FIN DE PLANTILLA
# ============================================================