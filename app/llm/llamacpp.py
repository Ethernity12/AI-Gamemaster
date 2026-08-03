from app.engine.settings import config
from app.llm.provider import LLMProvider
from llama_cpp import Llama


class LLamaCppProvider(LLMProvider):
    def __init__(self, model_path, n_gpu_layers, n_ctx, n_threads):
        self._llm = Llama(model_path=model_path, n_gpu_layers=n_gpu_layers, n_ctx=n_ctx, n_threads=n_threads, verbose=False)
        print(self._llm.chat_format)
        print(self._llm.metadata.get("tokenizer.chat_template"))

    async def generate(self, prompt):
        response = self._llm.create_chat_completion_openai_v1(
            max_tokens=2048,
            temperature=0.6,
            top_p=0.95,
            top_k=20,
            min_p=0,
            messages=[{"role": "user", "content": prompt}],
            chat_template_kwargs={
                "enable_thinking": False
            }
        )
        return response.choices[0].message.content
            
        
    