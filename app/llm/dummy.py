from typing import List

from app.llm.data_models import GenerationConfig, Message
from app.llm.provider import LLMProvider


class DummyLLMProvider(LLMProvider):
    def __init__(self, *args, **kwargs):
        pass

    async def generate(self, messages: List[Message], _config: GenerationConfig):
        return f"Dummy response to: {messages[-1].content}"