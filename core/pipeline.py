from .faiss_manager import load_vector_store
from .llm import get_llm
from .prompt import prompt
from .config import COLLEGE_PLACEHOLDER, TOP_K

from responses import PREDEFINED_RESPONSES

import time

from .logger import log_interaction
from .config import NO_INFORMATION_RESPONSE


vector_store = load_vector_store()

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": TOP_K,
        "fetch_k": 10,
        "lambda_mult": 0.7
    }
)

llm = get_llm()

chain = prompt | llm


def ask_question(question):

    start_time = time.perf_counter()

    question_lower = question.strip().lower()

    if question_lower in PREDEFINED_RESPONSES:

        response_time = round(
            time.perf_counter() - start_time,
            3
        )

        log_interaction(
            question=question,
            categories=[],
            documents=[],
            response_time=response_time,
            status="success",
            reason="predefined_response",
        )

        return {
            "answer": PREDEFINED_RESPONSES[question_lower],
            "sources": []
        }

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    context = context.replace(
        COLLEGE_PLACEHOLDER,
        "the college"
    )

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    answer = response.content.strip()

    sources = []

    categories = []

    for doc in docs:
        name = doc.metadata.get("document_name")
        category = doc.metadata.get("category")

        if name not in sources:
            sources.append(name)

        if category and category not in categories:
            categories.append(category)



    response_time = round(
        time.perf_counter() - start_time,
        3
    )        

    log_interaction(
        question=question,
        categories=categories,
        documents=sources,
        response_time=response_time,
        status="success",
    )

    if answer == NO_INFORMATION_RESPONSE:

        log_interaction(
            question=question,
            categories=categories,
            documents=sources,
            response_time=response_time,
            status="failed",
            reason="no_relevant_documents",
        )

    else:

        log_interaction(
            question=question,
            categories=categories,
            documents=sources,
            response_time=response_time,
            status="success",
        )

    return {
        "answer": answer,
        "sources": sources,
        
    }

