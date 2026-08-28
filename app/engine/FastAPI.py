from fastapi import FastAPI
from app.llm import provider
from app.database.connector import DatabaseConnector
from app.engine.settings import Settings

from contextlib import asynccontextmanager

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    database = DatabaseConnector(settings.postgres_url)
    await database.check_connection()
    app.state.database = database
    yield
    await database.close()

app = FastAPI(lifespan=lifespan)
llm_provider = provider.create_provider()

@app.get("/health")
async def api_status():
    database_ok = await app.state.database.check_health()

    return {
        "status": "ok" if database_ok else "degraded",
        "database": "ok" if database_ok else "unavailable",
    }

@app.post("/chat")
async def chat_endpoint(prompt: str):
    response = await llm_provider.generate(prompt)
    return {"response": response}