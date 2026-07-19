import streamlit as st

from .manager import (
    get_documents,
    delete_document,
)


def render_documents():
    """Render the document management page."""

    st.subheader("📄 Document Management")

    documents = get_documents()

    if not documents:
        st.info("No documents found.")
        return

    st.write(f"**Total Documents:** {len(documents)}")

    st.divider()

    for document in documents:
        col1, col2 = st.columns([8, 1])

        with col1:
            st.write(
                f"**{document['category']}** • 📄 {document['name']}"
            )

        with col2:
            if st.button(
               "🗑",
                key=f"delete_{document['name']}",
                help="Delete document",
            ):
                success, message = delete_document(document["path"])

                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)