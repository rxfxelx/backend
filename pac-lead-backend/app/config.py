from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    secret_key: str = "your-secret-key-here-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    database_url: str = "sqlite:///./pac_lead.db"
    openai_api_key: Optional[str] = None
    
    class Config:
        env_file = ".env"


settings = Settings()

