from app.llm.provider import LLMProvider


class LLamaCppProvider(LLMProvider):
    def __init__(self, *args, **kwargs):
        pass

    async def generate(self, prompt):
        return f"LlamaCpp response to: {prompt}"