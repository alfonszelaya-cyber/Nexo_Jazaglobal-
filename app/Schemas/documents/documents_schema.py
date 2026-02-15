# ============================================================
# ZYRA / NEXO
# DOCUMENTS SCHEMA — ENTERPRISE 3.0
# Digital Document Management Layer
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ============================================================
# CREATE DOCUMENT
# ============================================================

class CreateDocumentRequest(BaseModel):
    document_type: str  # INVOICE | CONTRACT | REPORT | RECEIPT
    title: str
    owner_id: str
    country: str
    currency: Optional[str]
    amount: Optional[float] = Field(default=0, ge=0)


class DocumentResponse(BaseModel):
    document_id: str
    document_type: str
    title: str
    owner_id: str
    status: str  # DRAFT | ISSUED | ARCHIVED
    created_at: datetime


# ============================================================
# DOCUMENT STATUS UPDATE
# ============================================================

class UpdateDocumentStatus(BaseModel):
    document_id: str
    new_status: str
    updated_at: datetime


# ============================================================
# DOCUMENT SUMMARY
# ============================================================

class DocumentSummary(BaseModel):
    total_documents: int
    active_documents: int
    archived_documents: int
    generated_at: datetime
