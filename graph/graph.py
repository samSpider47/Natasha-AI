
from langgraph.graph import StateGraph, START, END

from graph.state import GraphState
from graph.nodes import chatbot_node


def build_graph():
    """
    Build and compile the Natasha AI graph.
    """

    workflow = StateGraph(GraphState)

    # Register nodes
    workflow.add_node(
        "chatbot",
        chatbot_node
    )

    # Define flow
    workflow.add_edge(
        START,
        "chatbot"
    )

    workflow.add_edge(
        "chatbot",
        END
    )

    # Compile graph
    return workflow.compile()


graph = build_graph()
