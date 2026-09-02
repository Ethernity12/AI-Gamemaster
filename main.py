from fastapi import FastAPI
from app.llm import provider
from app.api.routes.chat import router as chat_router
from app.api.routes.session import router as session_router
from app.database.connector import DatabaseConnector
from app.services.session_service import SessionService
from app.database.repositories.session_repository import SessionRepository
from settings import Settings

from contextlib import asynccontextmanager

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    database = DatabaseConnector(settings.postgres_url)
    
    if not await database.check_health():
        raise RuntimeError("Database is unavailable")
    
    session_repository = SessionRepository(database)
    session_service = SessionService(session_repository)
    app.state.llm = provider.create_provider(settings)
    app.state.database = database
    app.state.session_service = session_service
    yield
    await database.close()

app = FastAPI(title="AI GameMaster API", lifespan=lifespan)

app.include_router(chat_router, prefix="/chat", tags=["Chat"])
app.include_router(session_router, prefix="/sessions", tags=["Sessions"])

@app.get("/health")
async def api_status():
    database_ok = await app.state.database.check_health()

    return {
        "status": "ok" if database_ok else "degraded",
        "database": "ok" if database_ok else "unavailable",
    }