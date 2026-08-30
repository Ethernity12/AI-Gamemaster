from typing import Protocol
from pathlib import Path
from os import cpu_count
from app.llm.data_models import GenerationConfig, Message


class LLMProvider(Protocol):
    async def generate(self, messages: list[Message], config: GenerationConfig | None = None) -> str:
        ...
        
def create_provider() -> LLMProvider:
    from app.engine.settings import Settings
    config = Settings()
    provider_name = config.llm_provider
    
    if provider_name == "dummy":
        from app.llm.dummy import DummyLLMProvider
    
        return DummyLLMProvider()
    
    elif provider_name == "api":
        from app.llm.api_provider import APILLMProvider
        
        return APILLMProvider(
            base_url=config["LLM_BASE_URL"],
            api_key=config.get("LLM_API_KEY", "local"),
            model=config["LLM_MODEL"],
        )
        
    raise ValueError(f"Unknown LLM provider: {provider_name}")