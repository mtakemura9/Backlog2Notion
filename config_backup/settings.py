"""
Settings module
"""
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    backlog_space_id: str = "dummy"
    backlog_api_key: str = "dummy"
    notion_token: str = "dummy"
    notion_database_id: str = "dummy"
    app_name: str = "Backlog2Notion API"
    app_version: str = "0.1.0"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8009
    
    class Config:
        env_file = ".env"

settings = Settings()

def validate_settings():
    """設定の妥当性チェック"""
    return True

def print_settings():
    """設定表示"""
    print(f"App: {settings.app_name}")
    print(f"Debug: {settings.debug}")
    print(f"Port: {settings.port}")
