from app.llm.provider import LLMProvider


class DummyLLMProvider(LLMProvider):
    def __init__(self, *args, **kwargs):
        pass

    async def generate(self, prompt):
        return f"Dummy response to: {prompt}"