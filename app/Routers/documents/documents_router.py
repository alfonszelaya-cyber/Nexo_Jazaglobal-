# ============================================================
# ZYRA / NEXO
# DOCUMENTS ROUTER — ENTERPRISE 3.0
# Document Management & Digital Records
# ============================================================

from fastapi import APIRouter, HTTPException
from datetime import datetime

# ============================================================
# IMPORT SCHEMAS
# ============================================================

from app.Schemas.documents.documents_schema import (
    DocumentsStatusResponse,
    CreateDocumentRequest,
    CreateDocumentResponse,
    GetDocumentRequest,
    GetDocumentResponse,
    DeleteDocumentRequest,
    DeleteDocumentResponse
)

# ============================================================
# IMPORT SERVICE  (CORREGIDO: Services en plural)
# ============================================================

from app.Services.documents.documents_services import DocumentsService


# ============================================================
# ROUTER INSTANCE
# ============================================================

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
        return documents_service.upload_document(
            owner_id=payload.owner_id,
            document_type=payload.document_type
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# GET DOCUMENT
# ============================================================

@router.post("/get", response_model=GetDocumentResponse)
def get_document(payload: GetDocumentRequest):
    try:
        return {
            "document_id": payload.document_id,
            "status": "retrieved",
            "retrieved_at": datetime.utcnow()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ============================================================
# DELETE DOCUMENT
# ============================================================

@router.post("/delete", response_model=DeleteDocumentResponse)
def delete_document(payload: DeleteDocumentRequest):
    try:
        return documents_service.archive_document(
            document_id=payload.document_id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
