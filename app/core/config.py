from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings

# Base directory of the app   
# アプリのベースディレクトリ
BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    #--------------------------
    #Path
    #--------------------------

    # Directory for log
    # ベクトルDB保存フォルダ
    LOG_DIR: Path = BASE_DIR / "app/logs"

    #--------------------------
    #API KEYz
    #--------------------------

    GEMINI_API_KEY: str

    #LOG Parameter
    LOG_LEVEL: str = "INFO"

    class Config():
        env_file = BASE_DIR / ".env"
        env_file_encoding = "utf-8"

    @field_validator("GEMINI_API_KEY")
    def validate_api_key(cls, v):
        if not v or v.strip() == "":
            raise ValueError("GEMINI_API_KEY is required")
        return v

settings = Settings()

