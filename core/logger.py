import json
from pathlib import Path

from core.config import BASE_DIR

from datetime import datetime, timedelta
from collections import Counter


LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "usage_logs.json"


# Public Functions------------------------------------------------------------------------------------

def initialize_logs():
    """
    Create the logs directory and usage_logs.json
    if they do not already exist.
    """

    LOG_DIR.mkdir(exist_ok=True)

    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def load_logs():
    """
    Load all interaction logs.
    """

    initialize_logs()

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    

def save_logs(logs):
    """
    Save interaction logs.
    """

    initialize_logs()

    with open(LOG_FILE, "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=4)



def log_interaction(
    question,
    categories,
    documents,
    response_time,
    status,
    reason=None,
):
    
    documents = documents or []
    categories = categories or []

    
    """
    Log a user interaction for analytics.
    """

    logs = load_logs()

    log_entry = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "question": question,
        "categories": categories,
        "documents": documents,
        "response_time": response_time,
        "status": status,
        "reason": reason,
    }

    logs.append(log_entry)

    save_logs(logs)


# Internal Helper Functions----------------------------------------------------------------------------

def _calculate_usage(logs):
    """
    Calculate usage statistics from interaction logs.
    """

    now = datetime.now()

    total_questions = len(logs)
    today_questions = 0
    weekly_questions = 0
    monthly_questions = 0

    for log in logs:

        timestamp = datetime.fromisoformat(log["timestamp"])

        if timestamp.date() == now.date():
            today_questions += 1

        if timestamp >= now - timedelta(days=7):
            weekly_questions += 1

        if (
            timestamp.year == now.year
            and timestamp.month == now.month
        ):
            monthly_questions += 1

    return {
        "total_questions": total_questions,
        "today_questions": today_questions,
        "weekly_questions": weekly_questions,
        "monthly_questions": monthly_questions,
    }



def _calculate_performance(logs):
    """
    Calculate performance statistics from interaction logs.
    """

    successful_retrievals = 0
    failed_retrievals = 0
    total_response_time = 0.0

    for log in logs:

        total_response_time += log["response_time"]

        if log["status"] == "success":
            successful_retrievals += 1
        else:
            failed_retrievals += 1

    average_response_time = 0.0

    if logs:
        average_response_time = round(
            total_response_time / len(logs),
            3
        )

    return {
        "average_response_time": average_response_time,
        "successful_retrievals": successful_retrievals,
        "failed_retrievals": failed_retrievals,
    }


def _calculate_categories(logs):
    """
    Calculate category statistics from interaction logs.
    """

    category_counter = Counter()

    for log in logs:

        for category in log.get("categories", []):
            category_counter[category] += 1

    most_asked_category = "N/A"

    if category_counter:
        most_asked_category = category_counter.most_common(1)[0][0]

    return {
        "most_asked_category": most_asked_category,
    }


def _calculate_documents(logs):
    """
    Calculate document statistics from interaction logs.
    """

    document_counter = Counter()

    for log in logs:

        for document in log.get("documents", []):
            document_counter[document] += 1

    most_accessed_document = "N/A"

    if document_counter:
        most_accessed_document = document_counter.most_common(1)[0][0]

    return {
        "most_accessed_document": most_accessed_document,
    }


def _calculate_activity(logs):
    """
    Calculate activity statistics from interaction logs.
    """

    last_question_time = "N/A"

    if logs:

        latest_log = max(
            logs,
            key=lambda log: datetime.fromisoformat(log["timestamp"])
        )

        last_question_time = latest_log["timestamp"]

    return {
        "last_question_time": last_question_time,
    }


def _calculate_knowledge_gaps(logs):
    """
    Calculate knowledge gap statistics from interaction logs.
    """

    unanswered_questions = 0

    for log in logs:

        if log.get("status") == "failed":
            unanswered_questions += 1

    return {
        "unanswered_questions": unanswered_questions,
    }


def get_statistics():
    """
    Collect all analytics statistics.
    """

    logs = load_logs()

    statistics = {}

    statistics.update(_calculate_usage(logs))
    statistics.update(_calculate_performance(logs))
    statistics.update(_calculate_categories(logs))
    statistics.update(_calculate_documents(logs))
    statistics.update(_calculate_activity(logs))
    statistics.update(_calculate_knowledge_gaps(logs))

    return statistics