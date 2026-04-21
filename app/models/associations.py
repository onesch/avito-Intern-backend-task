from sqlalchemy import Column, ForeignKey, Table

from app.models.base import Base


chat_user_association = Table(
    "chat_user_association",
    Base.metadata,
    Column("chat_id", ForeignKey("chats.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
)
