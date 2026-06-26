import os

from langchain_groq import ChatGroq
from pydantic import SecretStr
from dotenv import load_dotenv


load_dotenv()


class LLMAdapter:
    def __init__(
        self,
        model: str | None = None,
        temperature: float = 0.1,
    ) -> None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY is missing. ")

        self.llm = ChatGroq(
            api_key=SecretStr(api_key),
            model=model or os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            temperature=temperature,
        )

    def get_llm(self) -> ChatGroq:
        return self.llm
