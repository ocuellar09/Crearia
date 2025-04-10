from pydantic import BaseSettings

class Settings(BaseSettings):
    project_name: str = "Agente de Voz"
    environment: str = "development"
    log_level: str = "info"

    class Config:
        env_file = ".env"

settings = Settings()
