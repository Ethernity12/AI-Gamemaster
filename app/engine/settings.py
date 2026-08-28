from dotenv import dotenv_values
import os

class Settings:
    def __init__(self):
        self._config = {
            **dotenv_values(".env"),
            **os.environ
        }
    
    @property
    def postgres_host(self) -> str:
        return self._config.get("POSTGRES_HOST", "localhost")
    
    @property
    def postgres_port(self) -> int:
        return int(self._config.get("POSTGRES_PORT", 5432))
    
    @property
    def postgres_db(self) -> str:
        return self._config.get("POSTGRES_DB", "gamemaster")
    
    @property
    def postgres_user(self) -> str:
        return self._config.get("POSTGRES_USER", "gamemaster")
    
    @property
    def postgres_password(self) -> str:
        password = self._config.get("POSTGRES_PASSWORD")

        if not password:
            raise ValueError("POSTGRES_PASSWORD is not configured")

        return password
    
    @property
    def postgres_url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}"
            f"/{self.postgres_db}"
        )

    @property
    def llm_provider(self) -> str:
        return self._config.get("LLM_PROVIDER", "dummy")
    
    @property
    def api_base_url(self) -> str:
        return self._config.get("API_BASE_URL", "http://localhost:8000/")
    
    @property
    def api_key(self) -> str:
        return self._config.get("API_BASE_URL", "local")
    
    @property
    def llm_model(self) -> str:
        return self._config.get("LLM_MODEL", "dummy")


config = {
    **dotenv_values(".env"),
    **os.environ,
}