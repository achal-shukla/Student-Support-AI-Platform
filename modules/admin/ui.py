import streamlit as st

from .dashboard import render_dashboard
from .documents import render_documents
from .analytics import render_analytics

def render_admin_dashboard():
    st.title("🛠 Admin Dashboard")

    dashboard_tab, documents_tab, analytics_tab = st.tabs(
       [
        "📊 Dashboard",
        "📄 Documents",
        "📈 Analytics",
       ]
    )

    with dashboard_tab:
        render_dashboard()

    with documents_tab:
        render_documents()

    with analytics_tab:
        render_analytics()

