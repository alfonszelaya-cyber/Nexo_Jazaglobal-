# ============================================================
# payload_validator.py
# Validador universal y extensible de payloads
# ============================================================

def _fail(msg):
    return False, msg

def validate_required(payload: dict, required_fields: list):
    if not isinstance(payload, dict):
        return _fail("Payload inválido: no es dict")
    missing = [f for f in required_fields if f not in payload]
    if missing:
        return _fail(f"Campos faltantes: {missing}")
    return True, "OK"

def validate_schema(payload: dict, schema: dict):
    for field, field_type in schema.items():
        if field in payload and not isinstance(payload[field], field_type):
            return _fail(f"Campo '{field}' debe ser {field_type.__name__}")
    return True, "OK"

def validate_payload(payload: dict, required=None, schema=None):
    if required:
        ok, msg = validate_required(payload, required)
        if not ok:
            return ok, msg
    if schema:
        ok, msg = validate_schema(payload, schema)
        if not ok:
            return ok, msg
    return True, "VALID"
    
    
    
    
    # ============================================================
# payload_validator.py
# NEXO / ZYRA — VALIDACIÓN ESTRUCTURAL DE PAYLOADS
# CORE | CANÓNICO | INMUTABLE
# ============================================================
# Valida estructura contra un schema
# NO transforma datos
# NO ejecuta acciones
# ============================================================

from zyra_exceptions import ValidationError


def validate_payload(payload, schema):
    """
    Valida un payload contra un schema canónico.

    payload -> dict
    schema  -> dict (event_schema, contract_schema, etc)
    """

    if not isinstance(payload, dict):
        raise ValidationError("Payload no es un diccionario")

    for field, rules in schema.items():
        required = rules.get("required", False)

        if required and field not in payload:
            raise ValidationError(f"Campo requerido faltante: {field}")

        if field not in payload:
            continue

        value = payload[field]
        expected_type = rules.get("type")

        if expected_type == "STRING" and not isinstance(value, str):
            raise ValidationError(f"Campo {field} debe ser STRING")

        if expected_type == "DICT" and not isinstance(value, dict):
            raise ValidationError(f"Campo {field} debe ser DICT")

        if expected_type == "UUID" and not isinstance(value, str):
            raise ValidationError(f"Campo {field} debe ser UUID (string)")

        if expected_type == "ISO_DATETIME" and not isinstance(value, str):
            raise ValidationError(f"Campo {field} debe ser ISO_DATETIME")

        if expected_type == "ENUM":
            values = rules.get("values", [])
            if value not in values:
                raise ValidationError(
                    f"Campo {field} fuera de valores permitidos: {values}"
                )

    return True


# ============================================================
# NOTAS
# - La semántica la valida el CORE
# - Aquí solo se valida forma
# - Usado por event_router, audit, bus
# ============================================================
    