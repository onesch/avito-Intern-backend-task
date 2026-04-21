from datetime import datetime
from typing import List
from pydantic import BaseModel


class MessageCreate(BaseModel):
    """
    Schema for creating a message.

    Attributes:
        chat_id (int): Unique chat id.
        author_id (int): Unique user id.
        text (str): Text of the message.
    """
    chat_id: int
    author_id: int
    text: str


class MessageResponse(BaseModel):
    """
    Schema for message response returned from API.

    Attributes:
        id (int): Unique message ID.
        text (str): Text of the message.
        created_at (datetime): Timestamp when chat was created.
    """
    id: int
    text: str
    created_at: datetime

    class Config:
        from_attributes = True
