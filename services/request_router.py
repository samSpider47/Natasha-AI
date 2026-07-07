
from enum import Enum

from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from services.llm_service import llm_service


class Route(Enum):

    CHAT = "chat"

    RAG = "rag"


ROUTER_PROMPT = """
You are an AI request classifier.

Your ONLY task is deciding whether the assistant
should answer normally or retrieve information
from uploaded documents.

Return ONLY ONE WORD.

chat

or

rag

Rules

Choose rag if:

- the user is asking about an uploaded document
- the user refers to "this document"
- the user says "summarize"
- the user asks about a report
- the user asks about a PDF
- the user asks follow-up questions about the document
- the conversation is clearly still discussing the uploaded document

Choose chat if:

- general conversation
- greetings
- coding questions
- brainstorming
- writing
- general knowledge
- anything unrelated to uploaded documents

Return only

chat

or

rag
"""


class RequestRouter:

    def route(
        self,
        history: list[dict]
    ) -> Route:

        conversation = ""

        # Use only the last few messages to keep the prompt compact.
        recent_messages = history[-6:]

        for message in recent_messages:

            role = message["role"].capitalize()

            conversation += (
                f"{role}: {message['content']}\n"
            )

        response = llm_service.llm.invoke(

            [

                SystemMessage(
                    content=ROUTER_PROMPT
                ),

                HumanMessage(
                    content=conversation
                )

            ]

        )

        decision = response.content.strip().lower()

        if decision == "rag":

            return Route.RAG

        return Route.CHAT


request_router = RequestRouter()
