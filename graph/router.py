
from graph.state import NatashaState


def route_request(
    state: NatashaState,
) -> str:
    """
    Returns the next node to execute.

    LangGraph will use this function
    for conditional routing.
    """

    return state["route"]
