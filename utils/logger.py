"""
ログ設定とユーティリティ
"""

import logging
import sys
from pathlib import Path
from typing import Optional

def setup_logging(
    log_level: str = "INFO",
    log_file: Optional[str] = None,
    log_format: Optional[str] = None
) -> None:
    """ログ設定を初期化"""
    
    if log_format is None:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # ログレベル設定
    level = getattr(logging, log_level.upper(), logging.INFO)
    
    # ハンドラー設定
    handlers = [logging.StreamHandler(sys.stdout)]
    
    if log_file:
        # ログディレクトリ作成
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_file))
    
    # ログ設定
    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=handlers,
        force=True  # 既存の設定を上書き
    )

def get_logger(name: str) -> logging.Logger:
    """ロガーを取得"""
    return logging.getLogger(name)

# アプリケーション用ロガー
app_logger = get_logger("backlog2notion")
