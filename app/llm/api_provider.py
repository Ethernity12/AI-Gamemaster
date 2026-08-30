from app.llm.data_models import GenerationConfig, Message
from app.llm.provider import LLMProvider

import httpx


class APILLMProvider(LLMProvider):
    def __init__(self, api_url: str, api_port: int, api_key: str, model: str):
        self.api_url: str = api_url
        self.api_port: int = api_port
        self.api_key: str = api_key
        self.model: str = model
        
        self._client = httpx.AsyncClient(
            base_url=f"{self.api_url}:{self.api_port}",
            timeout=httpx.Timeout(connect=10.0, read=300.0, write=10.0, pool=10.0)
        )
    
    async def generate(self, messages: list[Message], config: GenerationConfig) -> str:
        response = await self._client.post(
            "/v1/chat/completions",
            json={
                "messages": [
                    {
                        "role": msg.role,
                        "content": msg.content,
                    }
                    for msg in messages
                ],
                "temperature": config.temperature,
                "max_tokens": config.max_tokens,
            },
        )

        response.raise_for_status()

        data = response.json()
        
        print(data)

        content = data["choices"][0]["message"]["content"]

        return "No answer..." if content == '' else content