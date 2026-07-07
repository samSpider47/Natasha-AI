
from langchain_core.messages import HumanMessage, SystemMessage

from services.llm_service import llm_service


TITLE_PROMPT = """
You are a system that generates short conversation titles.

Rules:
- Maximum 5 words
- No punctuation
- No quotes
- No extra text
- Return only the title

Examples:
User: Explain LangGraph architecture
Title: LangGraph Architecture

User: Help me debug Python code
Title: Python Debugging

User: Plan a trip to Japan
Title: Japan Trip Planning
"""


class TitleService:
    """
    Generates AI-powered conversation titles.
    """

    def generate_title(self, first_message: str) -> str:

        messages = [
            SystemMessage(content=TITLE_PROMPT),
            HumanMessage(content=first_message)
        ]

        try:
            response = llm_service.llm.invoke(messages)
            title = response.content.strip()

            # safety fallback cleanup
            title = title.replace('"', "").replace("Title:", "").strip()

            if not title:
                return "New Chat"

            return title[:60]

        except Exception:
            return "New Chat"


title_service = TitleService()
