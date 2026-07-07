
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

from config.prompt_builder import prompt_builder
from documents.rag_service import rag_service
from graph.state import NatashaState
from services.llm_service import llm_service
from services.request_router import (
    Route,
    request_router,
)


# ---------------------------------------------------------
# Node 1
# ---------------------------------------------------------

def prepare_node(
    state: NatashaState,
) -> NatashaState:
    """
    Prepare the initial graph state.
    """

    state["route"] = "chat"
    state["document_context"] = ""
    state["system_prompt"] = ""
    state["response"] = ""

    return state


# ---------------------------------------------------------
# Node 2
# ---------------------------------------------------------

def router_node(
    state: NatashaState,
) -> NatashaState:
    """
    Decide whether the request
    needs RAG or normal chat.
    """

    if not rag_service.has_documents():

        state["route"] = "chat"

        return state

    route = request_router.route(
        state["messages"]
    )

    state["route"] = route.value

    return state


# ---------------------------------------------------------
# Node 3
# ---------------------------------------------------------

def rag_node(
    state: NatashaState,
) -> NatashaState:

    latest_question = ""

    for message in reversed(state["messages"]):

        if message["role"] == "user":
            latest_question = message["content"]
            break

    context = rag_service.retrieve_context(
        latest_question
    )

    print("\n========== RAG CONTEXT ==========")
    print(context)
    print("=================================\n")

    state["document_context"] = context

    return state


# ---------------------------------------------------------
# Node 4
# ---------------------------------------------------------

def prompt_node(
    state: NatashaState,
) -> NatashaState:
    """
    Build the final system prompt.
    """

    state["system_prompt"] = (
        prompt_builder.build(
            state["document_context"]
        )
    )

    return state


# ---------------------------------------------------------
# Node 5
# ---------------------------------------------------------

def response_node(
    state: NatashaState,
) -> NatashaState:
    """
    Generate the assistant response.
    """

    messages = [

        SystemMessage(
            content=state["system_prompt"]
        )

    ]

    for message in state["messages"]:

        if message["role"] == "user":

            messages.append(

                HumanMessage(
                    content=message["content"]
                )

            )

        else:

            messages.append(

                AIMessage(
                    content=message["content"]
                )

            )

    response = llm_service.llm.invoke(
        messages
    )

    state["response"] = response.content

    return state
