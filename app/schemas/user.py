from datetime import datetime
from pydantic import BaseModel


class UserCreate(BaseModel):
    """
    Schema for creating a user.

    Attributes:
        username (str): Unique username of the user.
    """
    username: str


class UserResponse(BaseModel):
    """
    Schema for user response returned from API.

    Attributes:
        id (int): Unique user ID.
        username (str): Unique username of the user.
        created_at (datetime): Timestamp when user was created.
    """
    id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True
