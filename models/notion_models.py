"""
Notion API用データモデル
"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union

class NotionRichText(BaseModel):
    type: str = "text"
    text: Dict[str, str]
    annotations: Optional[Dict[str, Any]] = None
    plain_text: Optional[str] = None
    href: Optional[str] = None

class NotionTitle(BaseModel):
    title: List[NotionRichText]

class NotionNumber(BaseModel):
    number: Optional[Union[int, float]] = None

class NotionSelect(BaseModel):
    select: Optional[Dict[str, str]] = None

class NotionMultiSelect(BaseModel):
    multi_select: List[Dict[str, str]] = []

class NotionDate(BaseModel):
    date: Optional[Dict[str, str]] = None

class NotionPeople(BaseModel):
    people: List[Dict[str, Any]] = []

class NotionRichTextProperty(BaseModel):
    rich_text: List[NotionRichText]

class NotionProperty(BaseModel):
    """Notion プロパティの基底クラス"""
    pass

class NotionPage(BaseModel):
    parent: Dict[str, str]
    properties: Dict[str, Any]
    children: Optional[List[Dict[str, Any]]] = None

class NotionDatabase(BaseModel):
    id: str
    title: List[NotionRichText]
    properties: Dict[str, Any]
    parent: Dict[str, Any]
    url: str
    archived: bool
    created_time: str
    last_edited_time: str
