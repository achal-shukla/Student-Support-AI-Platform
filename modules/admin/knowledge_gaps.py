import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from core.logger import get_unanswered_questions



def show_knowledge_gaps():

    st.title("⚠️ Knowledge Gaps")

    st.caption(
        "Review unanswered student queries to identify missing information "
        "and improve the knowledge base."
    )

    st.divider()

    unanswered_questions = get_unanswered_questions()

    today = datetime.now().date()
    week_ago = today - timedelta(days=7)

    today_count = 0
    weekly_count = 0

    for log in unanswered_questions:
        log_date = datetime.fromisoformat(log["timestamp"]).date()

        if log_date == today:
            today_count += 1
 
        if log_date >= week_ago:
            weekly_count += 1


    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Knowledge Gaps",
            len(unanswered_questions)
        )

    with col2:
        st.metric(
            "Today",
            today_count
        )
    with col3:
        st.metric(
            "Past 7 Days",
            weekly_count
        )

    st.divider()





    if not unanswered_questions:
        st.success(
            "🎉 Great! The AI assistant answered all recent student queries."
        )
        return

    dataframe = pd.DataFrame(unanswered_questions)

    dataframe["timestamp"] = pd.to_datetime(
        dataframe["timestamp"]
    ).dt.strftime("%d %b %Y, %I:%M %p")

    reason_map = {
        "no_relevant_documents": "No Relevant Documents Found",
        "predefined_response": "Handled by Predefined Response",
    }

    dataframe["reason"] = dataframe["reason"].replace(reason_map)

    dataframe = dataframe[
       [
           "timestamp",
           "question",
           "reason",
        ]
    ]

    dataframe.columns = [
        "Asked On",
        "Student Question",
        "Reason",
    ]

    st.dataframe(
        dataframe,
        use_container_width=True,
        hide_index=True,
    )

    st.info(
        "💡 Review these unanswered queries regularly. "
        "Uploading documents that cover these topics will help improve the AI assistant's accuracy over time."
    )