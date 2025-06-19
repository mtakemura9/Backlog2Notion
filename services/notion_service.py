import requests
import os
from typing import Dict, Any
from utils.logger import get_logger

logger = get_logger(__name__)

class NotionService:
    def __init__(self):
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('NOTION_TOKEN')}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        self.database_id = os.getenv('NOTION_DATABASE_ID')
    
    def create_page(self, issue_data: Dict[Any, Any]) -> str:
        """シンプルなページ作成"""
        url = f"{self.base_url}/pages"
        
        # 最小限のプロパティ
        properties = {
            "Title": {
                "title": [{"text": {"content": issue_data["summary"][:100]}}]  # 長すぎる場合の対策
            },
            "ID": {
                "number": issue_data["id"]
            },
            "Status": {
                "rich_text": [{"text": {"content": issue_data["status"]["name"]}}]
            }
        }
        
        data = {
            "parent": {"database_id": self.database_id},
            "properties": properties
        }
        
        logger.info(f"Creating page for issue {issue_data['id']}")
        
        response = requests.post(url, json=data, headers=self.headers)
        response.raise_for_status()
        
        page_id = response.json()["id"]
        logger.info(f"Created page: {page_id}")
        return page_id
