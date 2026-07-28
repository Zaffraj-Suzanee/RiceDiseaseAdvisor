from langgraph.graph import StateGraph, END

from agents.planner_agent import planner_agent
from agents.router_agent import router_agent
from agents.retrieval_agent import retrieval_agent
from agents.reasoning_agent import reasoning_agent
from agents.reflection_agent import reflection_agent


def create_graph():

    workflow = StateGraph(dict)


    # Add agents
    workflow.add_node(
        "planner_agent",
        planner_agent
    )

    workflow.add_node(
        "router_agent",
        router_agent
    )

    workflow.add_node(
        "retrieval_agent",
        retrieval_agent
    )

    workflow.add_node(
        "reasoning_agent",
        reasoning_agent
    )

    workflow.add_node(
        "reflection_agent",
        reflection_agent
    )


    # Define flow

    workflow.set_entry_point(
        "planner_agent"
    )


    workflow.add_edge(
        "planner_agent",
        "router_agent"
    )


    workflow.add_edge(
        "router_agent",
        "retrieval_agent"
    )


    workflow.add_edge(
        "retrieval_agent",
        "reasoning_agent"
    )


    workflow.add_edge(
        "reasoning_agent",
        "reflection_agent"
    )


    workflow.add_edge(
        "reflection_agent",
        END
    )


    return workflow.compile()



def run_graph(question):

    app = create_graph()


    state = {

        "question": question,

        "messages": []

    }


    result = app.invoke(state)


    return result