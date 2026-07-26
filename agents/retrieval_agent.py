from rag.retrieve import retrieve_documents
from agents.messages import AgentMessage


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

      # Agent-to-agent communication message
    message: AgentMessage = {

        "sender": "retrieval_agent",

        "receiver": "reasoning_agent",

        "task": "provide_context",

        "content": {

            "documents_found": len(documents)

        },

        "status": "completed"

    }


    state["messages"].append(message)

    return state