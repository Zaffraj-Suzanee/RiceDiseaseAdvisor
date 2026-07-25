from typing import Dict

def router_agent(state: Dict):
    """
    Router Agent:
    Classifies the user's question.
    """

    question = state["question"].lower()

    if "symptom" in question:
        state["intent"] = "symptoms"

    elif "treatment" in question:
        state["intent"] = "treatment"

    elif "prevent" in question:
        state["intent"] = "prevention"

    else:
        state["intent"] = "general"

    return state