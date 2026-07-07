
from typing import List, TypedDict


class NatashaState(TypedDict):
    """
    Shared state flowing through the LangGraph workflow.
    Every node reads from and writes to this object.
    """

    # Complete conversation history
    messages: List[dict]

    # Router decision
    route: str

    # Retrieved RAG context
    document_context: str

    # Final system prompt
    system_prompt: str

    # Assistant response
    response: str
