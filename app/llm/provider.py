from typing import Protocol
from pathlib import Path
from os import cpu_count
from settings import Settings
from app.llm.data_models import GenerationConfig, Message


class LLMProvider(Protocol):
    async def generate(self, messages: list[Message], config: GenerationConfig | None = None) -> str:
        ...
        
def create_provider(config: Settings) -> LLMProvider:
    provider_name = config.llm_provider
    
    if provider_name == "dummy":
        from app.llm.dummy import DummyLLMProvider
    
        return DummyLLMProvider()
    
    elif provider_name == "api":
        from app.llm.api_provider import APILLMProvider
        
        return APILLMProvider(
            api_url=config.api_host,
            api_port=config.api_port,
            api_key=config.api_key,
            model=config.llm_model,
        )
        
    raise ValueError(f"Unknown LLM provider: {provider_name}")