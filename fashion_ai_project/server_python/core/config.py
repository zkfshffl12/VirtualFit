import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    DB_User: str = os.getenv("DB_USER", "FASHION")
    DB_Password: str = os.getenv("DB_PASSWORD", "oracle")
    DB_Host: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "1521")
    DB_SERVICE: str = os.getenv("DB_SERVICE", "XEBD2")

    @property
    def DATABASE_URL(self) -> str:
        # 오라클 공식 주소 
        return f"oracle+oracledb://{self.DB_User}:{self.DB_Password}@{self.DB_Host}:{self.DB_PORT}/?service_name={self.DB_SERVICE}" 

settings = Settings()