import httpx
import requests
import os
from dotenv import load_dotenv
load_dotenv()
from config.settings import settings
from typing import List, Dict, Any
from models.backlog_models import BacklogFilter, BacklogTicket, BacklogIssue
from utils.logger import get_logger

logger = get_logger(__name__)

class BacklogService:
    def __init__(self):
        self.base_url = f"https://{os.getenv('BACKLOG_SPACE_ID')}.backlog.com/api/v2"
        self.api_key = os.getenv('BACKLOG_API_KEY')
    
    async def fetch_issues(
        self,
        project_id: str,
        assignee_id: str = '',
        status_id: str = '',
        count: int = 20,
    ) -> List[BacklogIssue]:
        params = {
            "apiKey": self.api_key,
            "projectId[]": project_id,
            "count": count,
        }
        if assignee_id:
            params["assigneeId[]"] = assignee_id
        if status_id:
            params["statusId[]"] = status_id

        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{self.base_url}/issues", params=params)
            resp.raise_for_status()
            issues = resp.json()
            return [BacklogIssue(**issue) for issue in issues]
    
    def get_projects(self) -> List[Dict[Any, Any]]:
        """プロジェクト一覧取得"""
        url = f"{self.base_url}/projects"
        params = {"apiKey": self.api_key}
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    async def fetch_tickets(self, filter: BacklogFilter) -> List[BacklogTicket]:
        params = {
            "apiKey": self.api_key,
            "projectId[]": filter.project_id,
        }
        if filter.assignee_id:
            params["assigneeId[]"] = filter.assignee_id
        if filter.status:
            params["statusId[]"] = filter.status

        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{self.base_url}/issues", params=params)
            resp.raise_for_status()
            issues = resp.json()
            return [
                BacklogTicket(
                    id=issue["id"],
                    summary=issue["summary"],
                    description=issue.get("description"),
                    status=issue["status"]["name"],
                    assignee=issue["assignee"]["name"] if issue.get("assignee") else None,
                    url=f"https://{settings.backlog_space_id}.backlog.com/view/{issue['issueKey']}"
                )
                for issue in issues
            ]

    def format_issues_for_notion(self, issues: List[BacklogIssue]) -> str:
        if not issues:
            return "該当するチケットはありません。"
        lines = [
        "| チケット | 状態 | 担当者 |",
        "|:---|:---|:---|"
    ]
        for issue in issues:
            summary = issue.summary.replace("\n", " ")
            url = f"https://{settings.backlog_space_id}.backlog.com/view/{issue.issueKey}"
            status = issue.status.name if issue.status else "-"
            assignee = issue.assignee.name if issue.assignee else "-"
            lines.append(f"| [{summary}]({url}) | {status} | {assignee} |")
        return "\n".join(lines)
