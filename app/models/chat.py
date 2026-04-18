from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from .associations import chat_user_association

if TYPE_CHECKING:
    from app.models.user import User


class Chat(Base):
    """Chat between users."""
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(),
    )

    users: Mapped[List["User"]] = relationship(
        "User", secondary=chat_user_association, back_populates="chats",
    )
