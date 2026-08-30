from app.llm.data_models import GenerationConfig
from app.llm.provider import LLMProvider


class APILLMProvider(LLMProvider):
    def __init__(self, base_url: str, api_key: str, model: str):
        self.base_url: str = base_url
        self.api_key: str = api_key
        self.model: str = model
    async def generate(self, messages: list[dict], config: GenerationConfig):
        pass