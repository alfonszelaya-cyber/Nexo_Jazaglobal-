# ============================================================
# export_documents.py
# NEXO / ZYRA — EXPORT DOCUMENTS
# ============================================================

def generate_documents(export_id: str):
    return {
        "export_id": export_id,
        "documents": [
            "invoice",
            "packing_list",
            "bill_of_lading"
        ],
        "status": "GENERATED"
    }