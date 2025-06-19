"""
Backlog2Notion Data Models Package
"""

from .sync_models import SimpleSyncRequest, SyncResponse, SyncStatus

# 基本モデル
__all__ = [
    "SimpleSyncRequest",
    "SyncResponse", 
    "SyncStatus"
]

# 詳細モデル（必要に応じてインポート）
try:
    from .backlog_models import BacklogIssue, BacklogProject, BacklogUser, BacklogStatus
    from .notion_models import NotionPage, NotionProperty, NotionDatabase
    
    __all__.extend([
        "BacklogIssue",
        "BacklogProject", 
        "BacklogUser",
        "BacklogStatus",
        "NotionPage",
        "NotionProperty",
        "NotionDatabase"
    ])
except ImportError:
    # モデルファイルが未完成の場合はスキップ
    pass
