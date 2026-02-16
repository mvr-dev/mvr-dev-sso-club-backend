import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "SSO Club"
    database_url: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://user:password@db:5432/fastapi_db"
    )
    
    class Config:
        env_file = ".env"

settings = Settings()