from pydantic import BaseModel
from typing import Optional, List

class SimpleSyncRequest(BaseModel):
    """シンプル同期リクエスト"""
    project_id: Optional[int] = None
    status_ids: Optional[List[int]] = None
    limit: int = 10
    dry_run: bool = True

class SyncResponse(BaseModel):
    """同期レスポンス"""
    success: bool
    synced_count: int
    message: str
    errors: List[str] = []

class SyncStatus(BaseModel):
    """同期ステータス"""
    is_running: bool = False
    progress: int = 0
    total: int = 0
    current_issue: Optional[str] = None
    errors: List[str] = []
