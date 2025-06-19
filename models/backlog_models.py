"""
Backlog API用データモデル
"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class BacklogFilter(BaseModel):
    project_id: str
    assignee_id: Optional[str] = None
    status: Optional[str] = None

class BacklogTicket(BaseModel):
    id: int
    summary: str
    description: Optional[str]
    status: str
    assignee: Optional[str]
    url: str

class BacklogUser(BaseModel):
    id: int
    name: str
    roleType: int
    mailAddress: Optional[str] = None

class BacklogStatus(BaseModel):
    id: int
    name: str
    color: str
    displayOrder: int

class BacklogPriority(BaseModel):
    id: int
    name: str

class BacklogProject(BaseModel):
    id: int
    projectKey: str
    name: str
    chartEnabled: bool
    subtaskingEnabled: bool
    projectLeaderCanEditProjectLeader: bool
    textFormattingRule: str
    archived: bool
    displayOrder: int

class BacklogIssue(BaseModel):
    id: int
    projectId: int
    issueKey: str
    keyId: int
    issueType: Dict[str, Any]
    summary: str
    description: Optional[str] = None
    resolution: Optional[Dict[str, Any]] = None
    priority: BacklogPriority
    status: BacklogStatus
    assignee: Optional[BacklogUser] = None
    category: Optional[List[Dict[str, Any]]] = []
    versions: Optional[List[Dict[str, Any]]] = []
    milestone: Optional[List[Dict[str, Any]]] = []
    startDate: Optional[str] = None
    dueDate: Optional[str] = None
    estimatedHours: Optional[float] = None
    actualHours: Optional[float] = None
    parentIssueId: Optional[int] = None
    createdUser: BacklogUser
    created: str
    updatedUser: Optional[BacklogUser] = None
    updated: Optional[str] = None
    customFields: Optional[List[Dict[str, Any]]] = []
    attachments: Optional[List[Dict[str, Any]]] = []
    sharedFiles: Optional[List[Dict[str, Any]]] = []
    stars: Optional[List[Dict[str, Any]]] = []
