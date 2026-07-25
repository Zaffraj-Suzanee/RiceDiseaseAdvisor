from agents.planner_agent import planner_agent
from agents.router_agent import router_agent
from agents.retrieval_agent import retrieval_agent
from agents.reasoning_agent import reasoning_agent
from agents.reflection_agent import reflection_agent


def run_graph(question):

    state = {
        "question": question
    }

    state = planner_agent(state)

    state = router_agent(state)

    state = retrieval_agent(state)

    state = reasoning_agent(state)

    state = reflection_agent(state)

    return state