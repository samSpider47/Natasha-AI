
from langgraph.graph import (
    END,
    START,
    StateGraph,
)

from graph.router import route_request
from graph.state import NatashaState

from graph.nodes import (
    prepare_node,
    prompt_node,
    rag_node,
    response_node,
    router_node,
)


workflow = StateGraph(NatashaState)

# ---------------------------------------------------
# Nodes
# ---------------------------------------------------

workflow.add_node(
    "prepare",
    prepare_node,
)

workflow.add_node(
    "router",
    router_node,
)

workflow.add_node(
    "rag",
    rag_node,
)

workflow.add_node(
    "prompt",
    prompt_node,
)

workflow.add_node(
    "response",
    response_node,
)

# ---------------------------------------------------
# Edges
# ---------------------------------------------------

workflow.add_edge(
    START,
    "prepare",
)

workflow.add_edge(
    "prepare",
    "router",
)

workflow.add_conditional_edges(
    "router",
    route_request,
    {
        "chat": "prompt",
        "rag": "rag",
    },
)

workflow.add_edge(
    "rag",
    "prompt",
)

workflow.add_edge(
    "prompt",
    "response",
)

workflow.add_edge(
    "response",
    END,
)

graph = workflow.compile()
