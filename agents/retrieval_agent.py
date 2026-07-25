from rag.retrieve import retrieve_documents


def retrieval_agent(state):

    question = state["question"]

    documents = retrieve_documents(
        question,
        k=3
    )

    state["documents"] = [
        doc.page_content
        for doc in documents
    ]

    return state