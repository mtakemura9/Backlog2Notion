from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from models.sync_models import SimpleSyncRequest, SyncResponse
from fastapi import FastAPI, HTTPException

from models.backlog_models import BacklogFilter as BacklogFilterModel
from services.backlog_service import BacklogService
from config.settings import settings, validate_settings
from config.pip_config import setup_pip_config
from utils.logger import setup_logging, get_logger
import os


# pip設定を環境変数で設定
setup_pip_config()
# アプリ起動時の設定
def startup():
    """アプリケーション初期化"""
    try:
        # 環境変数チェック
        validate_settings()
        
        # ログ設定
        setup_logging(
            log_level=settings.log_level,
            log_file=os.getenv("LOG_FILE", "app.log")
        )
        
        logger = get_logger(__name__)
        logger.info(f"🚀 Starting {settings.app_name} v{settings.app_version}")
        logger.info(f"📡 Server: {settings.host}:{settings.port}")
        logger.info(f"🔧 Debug: {settings.debug}")
        
        return True
    except Exception as e:
        print(f"❌ Startup failed: {e}")
        return False

@asynccontextmanager
async def lifespan(app: FastAPI):
    if not startup():
        raise Exception("Failed to initialize application")
    yield  # ここでアプリが動き始める
    print("アプリが終了します！（lifespan）")

# アプリケーション初期化
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="BacklogとNotionを同期するAPI",
    lifespan=lifespan
)

logger = get_logger(__name__)


@app.get("/")
async def root():
    return {
        "message": f"{settings.app_name} v{settings.app_version}",
        "status": "running",
        "endpoints": ["/health", "/debug", "/simple-sync", "/projects"]
    }

@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": "2024-01-01T00:00:00Z"}

@app.get("/debug")
async def debug():
    """デバッグ情報"""
    return {
        "backlog_space": settings.backlog_space_id,
        "backlog_api_key": settings.backlog_api_key,
        "notion_database_id": settings.notion_database_id[:8] + "...",
        "sync_limit": settings.default_sync_limit,
        "max_limit": settings.max_sync_limit
    }

@app.post("/simple-sync")
async def simple_sync(request: SimpleSyncRequest):
    """シンプル同期（実装準備中）"""
    logger.info(f"Sync request: {request}")
    
    # バリデーション
    if request.limit > settings.max_sync_limit:
        raise HTTPException(
            status_code=400, 
            detail=f"Limit cannot exceed {settings.max_sync_limit}"
        )
    
    return SyncResponse(
        success=True,
        synced_count=0,
        message=f"準備中 - limit:{request.limit}, dry_run:{request.dry_run}",
        errors=[]
    )



app = FastAPI()
backlog_service = BacklogService()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.backlog_service import BacklogService

app = FastAPI()
backlog_service = BacklogService()

class BacklogFilter(BaseModel):
    project_id: str
    assignee_id: str
    status_id: str
    count: int = 20

@app.post("/get-backlog-by-filter")
async def get_backlog_by_filter(filter: BacklogFilter):
    try:
        issues = await backlog_service.fetch_issues(
            project_id=filter.project_id,
            assignee_id=filter.assignee_id,
            status_id=filter.status_id,
            count=filter.count,
        )
        notion_md = backlog_service.format_issues_for_notion(issues)
        return {"notion_markdown": notion_md}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host=settings.host, 
        port=settings.port,
        log_level=settings.log_level.lower()
    )
