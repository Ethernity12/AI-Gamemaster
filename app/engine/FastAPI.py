from fastapi import FastAPI
from app.llm import provider

app = FastAPI()
llm_provider = provider.create_provider()

@app.get("/health")
async def api_status():
    return {"status": "ok"}

@app.post("/chat")
async def chat_endpoint(prompt: str):
    response = await llm_provider.generate(prompt)
    return {"response": response}