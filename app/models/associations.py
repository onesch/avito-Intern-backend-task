from sqlalchemy import Column, ForeignKey, Table

from app.models.base import Base


chat_user_association = Table(
    "chat_user_association",
    Base.metadata,
    Column("chat_id", ForeignKey("chats.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
)

message_author_association = Table(
    "message_author_association",
    Base.metadata,
    Column("message_id", ForeignKey("messages.id"), primary_key=True),
    Column("author_id", ForeignKey("users.id"), primary_key=True),
)
