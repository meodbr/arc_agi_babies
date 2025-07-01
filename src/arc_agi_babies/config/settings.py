from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, ValidationError
import os
import sys


class Settings(BaseSettings):
    DEBUG: bool = Field(default=False, description="Enable debug mode")
    GEMINI_MODEL: str = Field(default="gemini-2.0-flash", description="Gemini model used for the agents")

    GOOGLE_CLOUD_PROJECT: str = Field(..., description="ID de projet GCP")
    GOOGLE_CLOUD_LOCATION: str = Field(..., description="Région GCP")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

try:
    settings = Settings()
except ValidationError as e:
    if not os.path.exists(".env"):
        print(
            ".env file not found! Please create one or copy from .env.example.",
            file=sys.stderr,
        )
    else:
        print("Configuration error:", file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)
