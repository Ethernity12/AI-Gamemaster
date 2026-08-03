from app.engine.settings import config
from app.llm.provider import LLMProvider
from llama_cpp import Llama


class LLamaCppProvider(LLMProvider):
    def __init__(self, model_path, n_gpu_layers, n_ctx, n_threads):
        self._llm = Llama(model_path=model_path, n_gpu_layers=n_gpu_layers, n_ctx=n_ctx, n_threads=n_threads)

    async def generate(self, prompt):
        response = self._llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],)
        
        return response['choices'][0]['message']['content']
            
        
    