# ============================================================
# ZYRA / NEXO
# DOCUMENTS ROUTER — ENTERPRISE 3.0
# Document Management & Digital Records
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================
# IMPORT SCHEMAS
# ============================

from app.Schemas.documents.documents_schema import (
    DocumentsStatusResponse,
    CreateDocumentRequest,
    CreateDocumentResponse,
    GetDocumentRequest,
    GetDocumentResponse,
    DeleteDocumentRequest,
    DeleteDocumentResponse
)

# ============================
# IMPORT SERVICE
# ============================

from app.Services.documents.documents_services import DocumentsServices


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

documents_service = DocumentsService()


# ============================================================
# STATUS
# ============================================================

@router.get("/status", response_model=DocumentsStatusResponse)
def documents_status():
    return DocumentsStatusResponse(
        module="ZYRA_DOCUMENTS_ENGINE",
        status="active",
        version="3.0.0",
        timestamp=datetime.utcnow()
    )


# ============================================================
# CREATE DOCUMENT
# ============================================================

@router.post("/create", response_model=CreateDocumentResponse)
def create_document(payload: CreateDocumentRequest):
    try:
        return documents_service.create_document(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# GET DOCUMENT
# ============================================================

@router.post("/get", response_model=GetDocumentResponse)
def get_document(payload: GetDocumentRequest):
    return documents_service.get_document(payload)


# ============================================================
# DELETE DOCUMENT
# ============================================================

@router.post("/delete", response_model=DeleteDocumentResponse)
def delete_document(payload: DeleteDocumentRequest):
    return documents_service.delete_document(payload)
