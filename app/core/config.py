from pydantic import BaseSettings

class Settings(BaseSettings):
    # Основные настройки
    PROJECT_NAME: str = "Auth Service"
    VERSION: str = "1.0.0"

    # Настройки базы данных
    DATABASE_URL: str = "sqlite:///./auth.db"

    # Настройки безопасности
    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

# Экземпляр настроек
settings = Settings()
