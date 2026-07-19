from pathlib import Path
import json

from core.config import VECTOR_STORE_DIR
from datetime import datetime

METADATA_FILE = VECTOR_STORE_DIR / "metadata.json"


def save_metadata(document_count, chunk_count):
    """Save knowledge base metadata."""

    metadata = {
        "documents": document_count,
        "chunks": chunk_count,
        "last_updated": datetime.now().isoformat(timespec="seconds"),
    }

    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)


def load_metadata():
    """Load knowledge base metadata."""

    if not METADATA_FILE.exists():
        return {
            "documents": 0,
            "chunks": 0,
            
        }

    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)