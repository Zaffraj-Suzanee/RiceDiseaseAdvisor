from agents.planner_agent import planner_agent
from agents.router_agent import router_agent


def run_graph(question):

    state = {
        "question": question
    }

    state = planner_agent(state)
    state = router_agent(state)

    return state