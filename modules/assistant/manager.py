"""
Assistant Manager

Future responsibilities:
- Chat processing
- Session management
- Conversation memory
- Prompt routing
"""
from core.pipeline import ask_question


def process_query(query: str):
    """
    Process a user query through the RAG pipeline.
    """
    return ask_question(query)