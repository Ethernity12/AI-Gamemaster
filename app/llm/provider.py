from typing import Protocol

class LLMProvider(Protocol):
    async def generate(self, prompt: str) -> str:
        ...
        
def create_provider() -> LLMProvider:
    from app.engine.settings import config
    provider_name = config.get("LLM_PROVIDER", "dummy").lower()
    
    if provider_name == "dummy":
        from app.llm.dummy import DummyLLMProvider
        return DummyLLMProvider()
    elif provider_name == "llamacpp":
        from app.llm.llamacpp import LLamaCppProvider
        return LLamaCppProvider()
    else:
        raise ValueError(f"Unknown LLM provider: {provider_name}")