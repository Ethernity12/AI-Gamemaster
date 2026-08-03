from typing import Protocol
from pathlib import Path
from os import cpu_count


class LLMProvider(Protocol):
    async def generate(self, prompt: str) -> str:
        ...
        
def create_provider() -> LLMProvider:
    from app.engine.settings import config
    provider_name = config.get("LLM_PROVIDER", "dummy").lower()
    
    fallback_model = Path(config.get('model_path', 'models'))
    fallback_model = str(next((fallback_model.glob("*.gguf")), None))
    
    if provider_name == "dummy":
        from app.llm.dummy import DummyLLMProvider
        return DummyLLMProvider()
    elif provider_name == "llamacpp":
        from app.llm.llamacpp import LLamaCppProvider
        return LLamaCppProvider(model_path=config.get('model_path', fallback_model),
                 n_gpu_layers=config.get('n_gpu_layers', -1), 
                 n_ctx=config.get('n_ctx', 8192), 
                 n_threads=config.get('n_threads', cpu_count()//2))
    else:
        raise ValueError(f"Unknown LLM provider: {provider_name}")