
import streamlit as st

from .manager import get_dashboard_stats


def render_dashboard():
    """Render the admin dashboard home page."""

    stats = get_dashboard_stats()

    st.title("📊 Dashboard")

    st.caption(
        "Monitor the overall health and activity of the Student Support AI Platform."
    )

    st.divider()

    # -----------------------------
    # Overview
    # -----------------------------

    st.subheader("📈 Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Documents",
            stats["documents"]
        )

    with col2:
        st.metric(
            "Knowledge Chunks",
            stats["chunks"]
        )

    with col3:
        st.metric(
            "Questions Answered",
            stats["questions"]
        )

    st.divider()

    # -----------------------------
    # System Status
    # -----------------------------

    st.subheader("⚙️ System Status")

    status_col1, status_col2 = st.columns(2)

    with status_col1:

        st.success("Knowledge Base Loaded")

        st.success(
            f"Vector Store : {stats['vector_store']}"
        )

    with status_col2:

        st.success(
            f"LLM Status : {stats['llm']}"
        )

        st.info(
            f"Last Updated\n\n{stats['last_updated']}"
        )