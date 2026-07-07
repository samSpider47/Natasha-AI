
from langchain_groq import ChatGroq

from config.settings import settings


class LLMService:
    """
    Singleton LLM service.
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance._llm = ChatGroq(
                model=settings.MODEL_NAME,
                temperature=settings.TEMPERATURE,
                api_key=settings.GROQ_API_KEY,
            )

        return cls._instance

    @property
    def llm(self):
        return self._llm


llm_service = LLMService()
