from datetime import datetime
from typing import List
from pydantic import BaseModel


class ChatCreate(BaseModel):
    """
    Schema for creating a chat.

    Attributes:
        name (str): Unique name of the chat.
        users (list[int]): Users id list.
    """
    name: str
    users: List[int]


class ChatResponse(BaseModel):
    """
    Schema for chat response returned from API.

    Attributes:
        id (int): Unique chat ID.
        name (str): Unique Name of the chat.
        created_at (datetime): Timestamp when chat was created.
    """
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True
