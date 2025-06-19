"""
Settings module - 完全版
"""
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # API基本設定
    backlog_space_id: str = os.getenv("BACKLOG_SPACE_ID", "dummy")
    backlog_api_key: str = os.getenv("BACKLOG_API_KEY", "dummy")
    notion_token: str = os.getenv("NOTION_TOKEN", "dummy")
    notion_database_id: str = os.getenv("NOTION_DATABASE_ID", "dummy")
    
    # アプリ設定
    app_name: str = "Backlog2Notion API"
    app_version: str = "0.1.0"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8009
    default_sync_limit: int = 10
    max_sync_limit: int = 100
    
    # ログ設定（これが足りなかった！）
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # その他よくある設定
    environment: str = "development"
    allowed_hosts: list = ["*"]
    cors_origins: list = ["*"]
    
    class Config:
        env_file = ".env"

# インスタンス作成
settings = Settings()

def validate_settings():
    """設定の妥当性チェック"""
    required_vars = ['backlog_space_id', 'backlog_api_key', 'notion_token', 'notion_database_id']
    for var in required_vars:
        if getattr(settings, var) == "dummy":
            print(f"⚠️  {var} is not configured")
    return True

def print_settings():
    """設定表示"""
    print(f"App: {settings.app_name}")
    print(f"Version: {settings.app_version}")
    print(f"Debug: {settings.debug}")
    print(f"Host: {settings.host}")
    print(f"Port: {settings.port}")
    print(f"Log Level: {settings.log_level}")
