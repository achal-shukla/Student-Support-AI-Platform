from pathlib import Path


from .uploader import save_uploaded_file
from .indexer import rebuild_index


from .metadata import load_metadata


def get_knowledge_base_stats():
    return load_metadata()




def add_document(uploaded_file):
    """
    Add a document to the knowledge base.

    Parameters
    ----------
    uploaded_file : UploadedFile
        Streamlit uploaded PDF.

    Returns
    -------
    Path
        Path to the uploaded document.
    """

    saved_path = save_uploaded_file(uploaded_file)

    try:
        rebuild_index()

    except Exception:
        # Future improvements:
        # TODO:
        # - Roll back the uploaded file
        # - Log the error
        # - Notify administrators
        raise

    return saved_path


