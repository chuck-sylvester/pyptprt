# ---------------------------------------------------------------------
# app/config.py
# ---------------------------------------------------------------------
# FastAPI application configuration using Pydantic data validation
# ---------------------------------------------------------------------

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",    # load from this file + actual env vars
        extra="ignore"      # silently ignore env vars that don't match a field
    )

    # Application
    app_name: str = "Python Patient Portal"
    app_version: str = 

