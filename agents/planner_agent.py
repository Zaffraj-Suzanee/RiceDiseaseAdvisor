from agents.messages import AgentMessage


def planner_agent(state):

    question = state["question"]

    # Initialize communication history
    if "messages" not in state:
        state["messages"] = []


    message: AgentMessage = {

        "sender": "planner_agent",

        "receiver": "router_agent",

        "task": "query_planning",

        "content": {
            "question": question,
            "plan": f"Retrieve information related to {question}"
        },

        "status": "completed"
    }


    state["messages"].append(message)


    state["plan"] = message["content"]["plan"]

    return state