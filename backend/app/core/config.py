import os
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

env = os.getenv('ENV', 'dev')
dotenv_file = f'.env.{env}'
load_dotenv(dotenv_file)


class Settings(BaseSettings):
    SECRET_KEY: str = Field(default='ultrahipermegaultrasecreta')
    ALGORITHM: str = Field(default='HS256')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60)
    MONGO_URI: str | None = Field(default='mongodb://localhost:27017/')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        fields = {
            'SECRET_KEY': {'env': 'SECRET_KEY'},
            'ALGORITHM': {'env': 'ALGORITHM'},
            'ACCESS_TOKEN_EXPIRE_MINUTES': {'env': 'ACCESS_TOKEN_EXPIRE_MINUTES'},
            'MONGO_URI': {'env': 'MONGO_URI'},
        }

settings = Settings()