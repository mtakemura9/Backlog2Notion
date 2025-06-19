from typing import Dict, Any, List
from utils.logger import get_logger

logger = get_logger(__name__)

class TransformService:
    @staticmethod
    def backlog_to_notion(backlog_issue: Dict[Any, Any]) -> Dict[Any, Any]:
        """BacklogのIssueをNotion用に変換"""
        try:
            return {
                "id": backlog_issue["id"],
                "summary": backlog_issue["summary"] or "No Title",
                "status": backlog_issue.get("status", {"name": "Unknown"}),
                "priority": backlog_issue.get("priority", {"name": "Normal"}),
                "assignee": backlog_issue.get("assignee", {}).get("name", "Unassigned"),
                "created": backlog_issue.get("created", ""),
                "updated": backlog_issue.get("updated", "")
            }
        except Exception as e:
            logger.error(f"Transform error for issue {backlog_issue.get('id', 'unknown')}: {e}")
            # 最小限のデータで返す
            return {
                "id": backlog_issue.get("id", 0),
                "summary": "Error in transformation",
                "status": {"name": "Error"}
            }
