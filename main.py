from fastapi import FastAPI
from app.llm import provider
from app.api.routes.chat import router as chat_router
from app.database.connector import DatabaseConnector
from settings import Settings

from contextlib import asynccontextmanager

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    database = DatabaseConnector(settings.postgres_url)
    await database.check_health()
    app.state.llm = provider.create_provider(settings)
    app.state.database = database
    yield
    await database.close()

app = FastAPI(title="AI GameMaster API", lifespan=lifespan)

app.include_router(chat_router, prefix="/chat", tags=["Chat"])

@app.get("/health")
async def api_status():
    database_ok = await app.state.database.check_health()

    return {
        "status": "ok" if database_ok else "degraded",
        "database": "ok" if database_ok else "unavailable",
    }