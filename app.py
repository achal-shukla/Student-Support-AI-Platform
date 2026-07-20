import streamlit as st

from modules.assistant import render_assistant
from modules.admin import render_admin_dashboard
from modules.admin.knowledge_gaps import show_knowledge_gaps

from components import (
   
    sidebar_heading,
    sidebar_item,
    sidebar_content,
)

from modules.knowledge_base.ui import render_knowledge_base
from modules.knowledge_base.manager import get_knowledge_base_stats


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Student Support AI Platform",
    page_icon="🎓",
    layout="wide",
)


# ==========================================
# Load CSS
# ==========================================

def load_css():
    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )


load_css()


# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.title("Student Support AI Platform")

    sidebar_heading("System Status")

    stats = get_knowledge_base_stats()

    sidebar_item(
        "Documents",
        str(stats["documents"]),
    )

    sidebar_item(
        "Knowledge Chunks",
         str(stats["chunks"]),
    )
    

    sidebar_heading("Embedding Model")
    sidebar_content("all-MiniLM-L6-v2")

    sidebar_heading("LLM")
    sidebar_content("Cohere Command-A")

    st.divider()

    sidebar_heading("Grounded AI")

    st.info(
        "This assistant answers questions only from official college documents. "
        "If the requested information is unavailable, it will let you know rather than guessing."
    )

    st.divider()

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    sidebar_heading("Navigation")

    page = st.radio(
        "",
        [
            "💬 AI Assistant", 
            "📚 Knowledge Base",
            "🛠 Admin Dashboard",
        ],
        label_visibility="collapsed",
    )


# ==========================================
# Session State
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================
# AI Assistant
# ==========================================

if page == "💬 AI Assistant":
    render_assistant()

# ==========================================
# Knowledge Base
# ==========================================

elif page == "📚 Knowledge Base":

    render_knowledge_base()

elif page == "🛠 Admin Dashboard":
    render_admin_dashboard()

elif page == "Knowledge Gaps":
    show_knowledge_gaps()