import streamlit as st

from .manager import (
    get_documents,
    delete_document,
)


def render_documents():
    """Render the document management page."""

    st.title("📄 Document Management")

    st.caption(
        "Manage the documents used by the AI assistant to answer student queries."
    )

    st.divider()

    documents = get_documents()

    if not documents:
        st.info("No documents found.")
        return

    col1, col2 = st.columns([1, 5])

    with col1:
        st.metric(
            "Documents",
            len(documents)
        )

    st.divider()

    st.subheader("📚 Available Documents")


    for document in documents:
        col1, col2 = st.columns([8, 1])


        with col1:
            st.markdown(
                f"""
             **📄 {document['name']}**

                🏷️ Category: `{document['category']}`
                 """
            )


        with col2:
            if st.button(
               "🗑 Delete",
                key=f"delete_{document['name']}",
                help="Delete document",
            ):
                success, message = delete_document(document["path"])

                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
        


    st.info(
         "💡 Deleting a document automatically rebuilds the knowledge base to keep search results up to date."
    )