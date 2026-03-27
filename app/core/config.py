import os
from pathlib import Path
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

class JwtSettings(BaseModel):
    private_key_path: Path = Field(
        default_factory=lambda: Path(os.getenv("PRIVATE_KEY_PATH", str(BASE_DIR / "certs" / "jwt-private.pem")))
    )
    public_key_path: Path = Field(
        default_factory=lambda: Path(os.getenv("PUBLIC_KEY_PATH", str(BASE_DIR / "certs" / "jwt-public.pem")))
    )
    algorithm :str = "RS256"
    access_token_expire_minutes :int = 5

class Settings(BaseSettings):
    app_name: str = "SSO Club"
    database_url: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://user:password@db:5432/fastapi_db"
    )
    
    class Config:
        env_file = ".env"

settings = Settings()
jwt_settings = JwtSettings()