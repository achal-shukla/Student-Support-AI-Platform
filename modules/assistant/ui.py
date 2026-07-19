import streamlit as st
from core.pipeline import ask_question
from components import (
    hero_section,
    feature_cards,
    question_cards,
)

def render_assistant():
    
    

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