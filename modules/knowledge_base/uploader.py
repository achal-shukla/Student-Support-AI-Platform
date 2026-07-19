
from core.config import UPLOAD_DIR


def save_uploaded_file(uploaded_file):
    """
    Save an uploaded PDF into the knowledge base.

    Parameters
    ----------
    uploaded_file : UploadedFile  
        Streamlit uploaded file object.

    Returns
    -------
    Path
        Path to the saved PDF.
    """

    # Validate file type
    if uploaded_file.type != "application/pdf":
        raise ValueError( "Invalid file type. Please upload a PDF document.")

    destination = UPLOAD_DIR / uploaded_file.name

    with open(destination, "wb") as f:
        f.write(uploaded_file.getbuffer())
    if destination.stat().st_size == 0:
        raise ValueError("The uploaded PDF was saved as an empty file.")
    
    print(f"Uploaded size : {uploaded_file.size}")
    print(f"Buffer length : {len(uploaded_file.getbuffer())}")
    print(f"Saved size : {destination.stat().st_size}")

    return destination