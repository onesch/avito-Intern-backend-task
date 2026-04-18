from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def create_user(db: Session, username: str) -> User:
    """Add new user to db and check user in database."""
    user = db.execute(
        select(User).where(User.username == username)
    ).scalars().first()

    if user:
        raise HTTPException(
            status_code=409,
            detail="user name already taken."
        )

    db_user = User(username=username)
    db.add(db_user)

    db.commit()
    db.refresh(db_user)

    return db_user
