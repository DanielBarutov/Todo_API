from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # База данных
    database_url: str = "sqlite:///./todo.db"

    # Настройки приложения
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    # CORS
    cors_origins: list = ["*"]

    # API
    api_v1_prefix: str = "/api/v1"
    project_name: str = "ToDo API"
    project_version: str = "1.0.0"

    # Настройки окружения
    class Config:
        env_file = ".env"


settings = Settings()
