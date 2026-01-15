import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    # Environment (fallback)
    environment: str = Field(
        default_factory=lambda: os.getenv("ENVIRONMENT", "development"),
        alias="ENVIRONMENT"
    )

    # Database
    db_host: str = Field(..., alias="DB_HOST")
    db_port: int = Field(..., alias="DB_PORT")
    db_name: str = Field(..., alias="DB_NAME")
    db_user: str = Field(..., alias="DB_USER")
    db_password: str = Field(..., alias="DB_PASSWORD")

    # Security
    jwt_secret: str = Field(..., alias="JWT_SECRET")
    jwt_expires_in: str = Field(..., alias="JWT_EXPIRES_IN")

    # Optional
    log_level: str = Field("info", alias="LOG_LEVEL")
    external_api_url: str | None = Field(None, alias="EXTERNAL_API_URL")
    external_api_key: str | None = Field(None, alias="EXTERNAL_API_KEY")

    model_config = SettingsConfigDict(
        env_file=".env.development",
        extra="ignore"
    )


settings = Settings()
