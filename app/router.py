# ============================================================
# ZYRA / NEXO
# API ROUTER — ENTERPRISE 3.0 FULL
# Finance + Security + Health
# ============================================================

from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import secrets
import string
import uuid
import hashlib
from datetime import datetime

from application.use_cases.finance.generate_sales_finance_report_use_case import (
    GenerateSalesFinanceReportUseCase,
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Core"]
)

# ============================================================
# HEALTH
# ============================================================

@router.get("/health")
def health_check():
    return {
        "status": "OK",
        "service": "NEXO_ZYRA_CORE",
        "timestamp": datetime.utcnow()
    }


# ============================================================
# FINANCE — SALES REPORT
# ============================================================

@router.post("/finance/sales-report")
def generate_sales_report(payload: Dict[str, Any]):

    try:
        use_case = GenerateSalesFinanceReportUseCase()
        result = use_case.execute(payload)

        return {
            "success": True,
            "data": result
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# SECURITY — GENERATE PASSWORD
# ============================================================

@router.get("/security/generate-password")
def generate_password(length: int = 16):

    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))

    return {
        "generated_password": password,
        "length": length
    }


# ============================================================
# SECURITY — GENERATE TOKEN
# ============================================================

@router.get("/security/generate-token")
def generate_token(length: int = 32):

    token = secrets.token_hex(length)

    return {
        "secure_token": token
    }


# ============================================================
# SECURITY — GENERATE NUMBER
# ============================================================

@router.get("/security/generate-number")
def generate_secure_number(digits: int = 8):

    number = ''.join(secrets.choice(string.digits) for _ in range(digits))

    return {
        "secure_number": number
    }


# ============================================================
# SECURITY — GENERATE UUID
# ============================================================

@router.get("/security/generate-uuid")
def generate_uuid():

    return {
        "uuid": str(uuid.uuid4())
    }


# ============================================================
# SECURITY — HASH SHA256
# ============================================================

@router.post("/security/hash")
def hash_data(payload: Dict[str, Any]):

    if "data" not in payload:
        raise HTTPException(status_code=400, detail="data field required")

    hashed = hashlib.sha256(payload["data"].encode()).hexdigest()

    return {
        "original": payload["data"],
        "sha256": hashed
}
