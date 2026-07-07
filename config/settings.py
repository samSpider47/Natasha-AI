
import os


class Settings:

    MODEL_NAME = "llama-3.3-70b-versatile"

    TEMPERATURE = 0.7

    MAX_TOKENS = 4096

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


settings = Settings()
