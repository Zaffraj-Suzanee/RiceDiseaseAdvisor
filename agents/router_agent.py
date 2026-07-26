from agents.messages import AgentMessage


def router_agent(state):

    question = state["question"]


    intent = "disease_information"


    message: AgentMessage = {

        "sender": "router_agent",

        "receiver": "retrieval_agent",

        "task": "retrieve_documents",

        "content": {

            "intent": intent,

            "query": question

        },

        "status": "completed"

    }


    state["messages"].append(message)


    state["intent"] = intent


    return state