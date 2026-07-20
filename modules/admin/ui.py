import streamlit as st

from .dashboard import render_dashboard
from .documents import render_documents
from .analytics import show_analytics
from .knowledge_gaps import show_knowledge_gaps

def render_admin_dashboard():
    st.title("🛠 Admin Dashboard")

    dashboard_tab, documents_tab, analytics_tab,gaps_tab = st.tabs(
       [
        "📊 Dashboard",
        "📄 Documents",
        "📈 Analytics",
        "⚠️ Knowledge Gaps",
       ]
    )

    with dashboard_tab:
        render_dashboard()

    with documents_tab:
        render_documents()

    with analytics_tab:
        show_analytics()

    with gaps_tab:
        show_knowledge_gaps()

