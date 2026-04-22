from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.chat import Chat
from app.models.message import Message
from app.models.user import User
from app.utils.utils import get_or_404


def create_message(
        db: Session, chat_id: int, author_id: int, text: str
) -> Message:
    """Send a message to the chat on behalf of the user."""
    # check user / chat
    db_user = get_or_404(db, User, author_id, "user")
    db_chat = get_or_404(db, Chat, chat_id, "chat")

    # add / return
    db_message = Message(
        chat_id=chat_id,
        author_id=author_id,
        text=text,
    )

    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    return db_message


def get_messages_by_chat_id(db: Session, chat_id: int) -> List[Chat]:
    """Get chat messages list."""
    # check chat
    db_chat = get_or_404(db, Chat, chat_id, "chat")

    # get messages
    db_messages = db.execute(
        select(Message).where(Message.chat_id == chat_id)
    ).scalars().all()

    return db_messages
