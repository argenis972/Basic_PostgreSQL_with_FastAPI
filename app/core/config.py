from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    ENV: str = Field(default="dev")  # dev | test | prod
    DATABASE_URL: str
    LOG_LEVEL: str = Field(default="INFO")


settings = Settings()

