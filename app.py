import streamlit as st

from core.pipeline import ask_question
from components import (
    hero_section,
    feature_cards,
    question_cards,
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

    # Hero
    hero_section()

    # Features
    feature_cards()

    # Popular Questions
    if not st.session_state.messages:
        selected_question = question_cards()
    else:
        selected_question = None

    # Conversation History
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if message["role"] == "assistant":

                sources = message.get("sources", [])

                if sources:
                    with st.expander("📄 Sources"):
                        for source in sources:
                            st.write(f"• {source}")

    # Chat Input
    typed_question = st.chat_input(
        "Ask about admissions, hostel, fees, scholarships..."
    )

    query = selected_question or typed_question

    # Process Query
    if query:

        # User Message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": query,
            }
        )

        with st.chat_message("user"):
            st.markdown(query)

        # Assistant Response
        with st.chat_message("assistant"):

            with st.spinner("Looking through official college documents..."):
                result = ask_question(query)

            st.markdown(result["answer"])

            if result["sources"]:
                with st.expander("📄 Sources"):
                    for source in result["sources"]:
                        st.write(f"• {source}")

        # Save Assistant Response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result["answer"],
                "sources": result["sources"],
            }
        )

        st.rerun()


# ==========================================
# Knowledge Base
# ==========================================

elif page == "📚 Knowledge Base":

    render_knowledge_base()