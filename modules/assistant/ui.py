import streamlit as st
from .manager import process_query
from components import (
    hero_section,
    feature_cards,
    question_cards,
)

def render_header():
    """Render the assistant header section."""
    hero_section()
    feature_cards()


def render_popular_questions():
    """Render suggested questions before the conversation starts."""
    if not st.session_state.messages:
        return question_cards()
    return None

def render_chat_history():
    """Render the conversation history."""

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if message["role"] == "assistant":

                sources = message.get("sources", [])

                if sources:
                    with st.expander("📄 Sources"):
                        for source in sources:
                            st.write(f"• {source}")

def handle_chat_interaction(selected_question):
    """Handle a new chat interaction."""

    typed_question = st.chat_input(
        "Ask about admissions, hostel, fees, scholarships..."
    )

    query = selected_question or typed_question

    if not query:
        return

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
            result = process_query(query)

        st.markdown(result["answer"])

        if result["sources"]:
            with st.expander("📄 Sources"):
                for source in result["sources"]:
                    st.write(f"• {source}")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"],
            "sources": result["sources"],
        }
    )

    st.rerun()

def render_assistant():

    render_header()

    selected_question = render_popular_questions()

    # Conversation History

    render_chat_history()

    # Chat Input
    handle_chat_interaction(selected_question)
    