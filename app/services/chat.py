from typing import List

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.chat import Chat
from app.models.user import User
from app.utils.utils import get_or_404


def create_chat(db: Session, name: str, users: list[int]) -> Chat:
    """Add new chat to db and check chat name, user in database."""
    # check chat name
    chat = db.execute(
        select(Chat).where(Chat.name == name)
    ).scalars().first()

    if chat:
        raise HTTPException(
            status_code=409,
            detail="chat name already taken."
        )

    # create chat
    db_chat = Chat(name=name)

    # get users
    db_users = db.execute(
        select(User).where(User.id.in_(users))
    ).scalars().all()

    # check users
    if len(db_users) != len(users):
        raise HTTPException(
            status_code=404,
            detail="some users not found."
        )

    # many-to-many
    db_chat.users = db_users

    # add / return
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)

    return db_chat


def get_chats_by_user_id(db: Session, user_id: int) -> List[Chat]:
    """Get user chat objects list."""
    # get / check user
    db_user = get_or_404(db, User, user_id, "user")

    return db_user.chats
