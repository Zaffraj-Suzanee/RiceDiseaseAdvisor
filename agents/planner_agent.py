from typing import Dict

def planner_agent(state: Dict):
    """
    Planner Agent:
    Reads the user's question and creates a simple plan.
    """

    question = state["question"]

    state["plan"] = (
        f"Retrieve information related to: {question}"
    )

    return state