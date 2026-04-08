from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    # App
    APP_NAME: str = 'BakeArr'
    DEBUG: bool = False

    #Database
    DATABASE_URL: str = "sqlite:///./test.db" #no default - required, app won't start without it.

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Auth
    SECRET_KEY: str = "your-secret-key-here" # required - generate with: python -c "import secrets; print(secrets.token_hex(32))"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
