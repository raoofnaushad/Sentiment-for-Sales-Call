from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    openai_api_key: str
    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int
    mail_server: str

    class Config:
        env_file = ".env"

settings = Settings()

