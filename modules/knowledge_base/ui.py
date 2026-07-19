import streamlit as st

from .manager import add_document


def render_knowledge_base():
    """
    Render the Knowledge Base management interface.
    """

    st.subheader("📚 Knowledge Base")

    st.write(
        "Upload official college PDF documents to extend the knowledge base."
    )

    uploaded_file = st.file_uploader(
        "Choose a PDF document",
        type=["pdf"],
    )

    if uploaded_file is not None:

        with st.spinner("Updating the knowledge base..."):
            saved_path = add_document(uploaded_file)

            try:

                saved_path = add_document(uploaded_file)

                st.success(
                    f"'{saved_path.name}' was added successfully.\n\n"
                    "The knowledge base has been updated and the document is now searchable."
                )

            
            except ValueError as e:
                st.error(str(e))

            except Exception:
                st.error(
                     "An unexpected error occurred while uploading the document."
                      )

                