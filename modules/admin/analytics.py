
import streamlit as st

from core.logger import get_statistics
import pandas as pd


def show_analytics():
    """
    Display analytics dashboard.
    """

    st.subheader("📊 Analytics Dashboard")

    statistics = get_statistics()

    # Usage Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Questions",
            statistics["total_questions"]
        )

    with col2:
        st.metric(
            "Today's Questions",
            statistics["today_questions"]
        )

    with col3:
        st.metric(
            "Weekly Questions",
            statistics["weekly_questions"]
        )

    with col4:
        st.metric(
            "Monthly Questions",
            statistics["monthly_questions"]
        )

    # Performance Metrics
    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Response Time",
            f'{statistics["average_response_time"]} sec'
        )

    with col2:
        st.metric(
            "Successful Retrievals",
            statistics["successful_retrievals"]
        )

    with col3:
        st.metric(
            "Failed Retrievals",
            statistics["failed_retrievals"]
        )

    # Knowledge Base Metrics
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Most Asked Category",
            statistics["most_asked_category"]
        )

    with col2:
        st.metric(
            "Most Accessed Document",
            statistics["most_accessed_document"]
        )

    st.divider()

    st.subheader("📊 Questions by Category")

    category_counts = statistics["category_counts"]

    if category_counts:

        category_df = pd.DataFrame(
            category_counts.items(),
            columns=["Category", "Questions"]
        )

        category_df = category_df.sort_values(
            by="Questions",
            ascending=False
        )

        st.bar_chart(
            category_df.set_index("Category")
        )

    else:
        st.info("No category data available.")



    st.divider()

    st.subheader("📄 Most Accessed Documents")

    document_counts = statistics["document_counts"]

    if document_counts:

        document_df = pd.DataFrame(
            document_counts.items(),
            columns=["Document", "Access Count"]
        )

        document_df = document_df.sort_values(
            by="Access Count",
            ascending=False
        )

        st.bar_chart(
            document_df.set_index("Document")
        )

    else:
        st.info("No document usage data available.")

    # Activity Metrics
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Last Question",
            statistics["last_question_time"]
        )

    with col2:
        st.metric(
            "Unanswered Questions",
            statistics["unanswered_questions"]
        )
