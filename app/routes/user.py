from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.services.user import create_user
from app.database.database import get_db


router = APIRouter(tags=["users"])


@router.post(
    "/create-user",
    response_model=UserResponse,
    summary="Create a new user",
    description="Creates a new user in the database using provided username."
)
def create_user_endpoint(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    """
    Returns created user object with id and timestamp.

    - username: unique username for the user
    """
    return create_user(username=user.username, db=db)
