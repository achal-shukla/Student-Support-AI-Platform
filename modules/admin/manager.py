from modules.knowledge_base.manager import get_knowledge_base_stats
from pathlib import Path

from modules.knowledge_base.indexer import rebuild_index

#Dashboard -------------------------------------------------------------

def get_dashboard_stats():
    """Return all dashboard statistics."""

    kb_stats = get_knowledge_base_stats()

    return {
        "documents": kb_stats["documents"],
        "chunks": kb_stats["chunks"],
        "last_updated": kb_stats.get("last_updated", "Never"),
        "questions": 0,                  # Placeholder
        "vector_store": "Loaded",        # Placeholder
        "llm": "Connected",              # Placeholder
    }

# Document -------------------------------------------------------------                  

from core.config import DATA_DIR

from core.config import DATA_DIR


def get_documents():
    """Return all documents in the knowledge base."""

    documents = []

    for pdf in sorted(DATA_DIR.rglob("*.pdf")):
        documents.append(
            {
                "category": pdf.parent.name,
                "name": pdf.name,
                "path": pdf,
            }
        )

    return documents

#delete documents----------------------------------------------------------

def delete_document(document_path):
    """
    Delete a document from the knowledge base and rebuild the vector store.

    Args:
        document_path (str | Path): Path to the PDF.

    Returns:
        tuple[bool, str]:
            (True, success_message)
            (False, error_message)
    """

    try:
        document_path = Path(document_path)

        if not document_path.exists():
            return False, "Document not found."

        document_path.unlink()

        # Rebuild the knowledge base
        rebuild_index()

        return True, f"{document_path.name} deleted successfully."

    except Exception as e:
        return False, str(e)
    

# analysis---------------------------------------------------------------------


def get_analytics():
    """
    Return analytics data for the Admin dashboard.
    """

    return {
        "total_questions": 0,
        "today_questions": 0,
        "weekly_questions": 0,
        "monthly_questions": 0,
        "average_response_time": 0.0,
        "most_asked_category": "N/A",
        "most_accessed_document": "N/A",
    }