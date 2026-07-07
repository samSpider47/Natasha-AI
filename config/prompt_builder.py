
from config.prompts import (
    SYSTEM_PROMPT,
    RAG_PROMPT,
)


class PromptBuilder:
    """
    Builds the system prompt dynamically
    depending on the current conversation.
    """

    def build(
        self,
        document_context: str = ""
    ) -> str:

        prompt = SYSTEM_PROMPT.strip()

        if document_context:

            prompt += "\n\n"

            prompt += RAG_PROMPT.strip()

            prompt += "\n\n"

            prompt += (
                "DOCUMENT CONTEXT\n"
                "----------------\n"
            )

            prompt += document_context

        return prompt


prompt_builder = PromptBuilder()
