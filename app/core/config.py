from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "TrustAI"
    APP_VERSION: str = "1.0.0"

    DATABASE_URL: str = "sqlite:///./trustai.db"

    MODEL_NAME: str = "qwen3:8b"

    CONFIDENCE_THRESHOLD: float = 0.75

    class Config:
        env_file = ".env"


settings = Settings()