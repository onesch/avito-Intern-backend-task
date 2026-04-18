from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.chat import Chat
from app.models.user import User


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

    # check user
    if len(db_users) != len(users):
        raise HTTPException(
            status_code=404,
            detail="some users not found"
        )

    # many-to-many
    db_chat.users = db_users

    # add / return
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)

    return db_chat
