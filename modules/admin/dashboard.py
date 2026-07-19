
import streamlit as st

from .manager import get_dashboard_stats

def render_dashboard():
    """Render the admin dashboard home page."""

    stats = get_dashboard_stats()

    st.subheader("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Documents", stats["documents"])

    with col2:
        st.metric("🧩 Chunks", stats["chunks"])

    with col3:
        st.metric("💬 Questions", stats["questions"])

    st.divider()

    st.subheader("⚙️ System Status")

    st.write(f"**Last Updated:** {stats['last_updated']}")
    st.write(f"**Vector Store:** 🟢 {stats['vector_store']}")
    st.write(f"**LLM Status:** 🟢 {stats['llm']}")