from core.document_processor import (
    load_documents,
    split_documents,
)
from core.faiss_manager import create_vector_store
from core.config import DATA_DIR
from .metadata import save_metadata


def rebuild_index():
    """
    Rebuild the FAISS vector store using all documents
    available in the data directory.
    """

    print("Loading documents...")
    documents = load_documents()
    print(f"Loaded {len(documents)} pages.")

    print("\nSplitting documents...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    print("\nCreating vector store...")
    create_vector_store(chunks)

    # Count all indexed PDF files
    pdf_count = len(list(DATA_DIR.rglob("*.pdf")))

    save_metadata(
        document_count=pdf_count,
        chunk_count=len(chunks),
    )

    print("\n✅ Vector store rebuilt successfully.")