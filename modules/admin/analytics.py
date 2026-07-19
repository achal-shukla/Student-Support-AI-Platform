import streamlit as st

from .manager import get_analytics


def render_analytics():

    st.subheader("📈 Analytics")

    analytics = get_analytics()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Questions",
            analytics["total_questions"],
        )

        st.metric(
            "Today's Questions",
            analytics["today_questions"],
        )

        st.metric(
            "Weekly Questions",
            analytics["weekly_questions"],
        )

    with col2:
        st.metric(
            "Monthly Questions",
            analytics["monthly_questions"],
        )

        st.metric(
            "Avg Response Time",
            f"{analytics['average_response_time']} s",
        )

    st.divider()

    st.write(
        f"**Most Asked Category:** {analytics['most_asked_category']}"
    )

    st.write(
        f"**Most Accessed Document:** {analytics['most_accessed_document']}"
    )