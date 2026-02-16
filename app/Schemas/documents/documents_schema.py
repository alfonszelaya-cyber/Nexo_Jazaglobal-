# ============================================================
# ZYRA / NEXO
# DOCUMENTS SCHEMA — ENTERPRISE 3.0
# File: app/Schemas/documents/documents_schema.py
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ============================================================
# STATUS RESPONSE
# ============================================================

class DocumentsStatusResponse(BaseModel):
    module: str
    status: str
    version: str
    timestamp: datetime


# ============================================================
# CREATE DOCUMENT
# ============================================================

class CreateDocumentRequest(BaseModel):
    owner_id: str = Field(..., description="Owner of the document")
    document_type: str = Field(..., description="Type of document")
    description: Optional[str] = None


class CreateDocumentResponse(BaseModel):
    document_id: str
    owner_id: str
    document_type: str
    status: str
    created_at: datetime


# ============================================================
# GET DOCUMENT
# ============================================================

class GetDocumentRequest(BaseModel):
    document_id: str


class GetDocumentResponse(BaseModel):
    document_id: str
    owner_id: Optional[str] = None
    document_type: Optional[str] = None
    status: str
    retrieved_at: datetime


# ============================================================
# DELETE DOCUMENT
# ============================================================

class DeleteDocumentRequest(BaseModel):
    document_id: str


class DeleteDocumentResponse(BaseModel):
    document_id: str
    status: str
    deleted_at: datetime


# ============================================================
# LIST DOCUMENTS
# ============================================================

class DocumentItem(BaseModel):
    document_id: str
    document_type: str
    status: str
    created_at: datetime


class ListDocumentsResponse(BaseModel):
    total: int
    documents: List[DocumentItem]
    generated_at: datetime
