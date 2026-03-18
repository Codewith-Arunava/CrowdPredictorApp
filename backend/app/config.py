from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "CrowdPredictorApp"
    DEBUG: bool = True

    # JWT
    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "HS256"

    # Database (SQLite for now)
    DATABASE_URL: str = "sqlite:///./crowd.db"

settings = Settings()