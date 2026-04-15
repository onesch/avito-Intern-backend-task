from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def create_user(db: Session, username: str) -> User:
    """Add new user to db and check user in database."""
    with db.begin():  # execution in one transaction, get and add user.
        query = select(User).where(User.username == username)
        user = db.execute(query).scalars().first()

        if not user:
            db_user = User(username=username)

            db.add(db_user)
            db.commit()
            db.refresh(db_user)

            return db_user
        else:
            detail = "user name already taken."
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=detail,
            )
