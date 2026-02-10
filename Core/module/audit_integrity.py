# audit_integrity.py
# NEXO / ZYRA — AUDITORÍA & TRAZABILIDAD
# INTEGRIDAD DE REGISTROS
# PASIVO

import hashlib
import json

def hash_record(record: dict) -> str:
    """
    Genera hash SHA256 de un registro de auditoría.
    """
    payload = json.dumps(record, sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()