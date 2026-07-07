from typing import Generator, List

from graph.workflow import graph


class ChatService:
    """
    Chat service backed by LangGraph.
    """

    def stream_message(
        self,
        history: List[dict],
    ) -> Generator[str, None, None]:

        state = {
            "messages": history,
            "route": "",
            "document_context": "",
            "system_prompt": "",
            "response": "",
        }

        result = graph.invoke(state)

        yield result["response"]


chat_service = ChatService()