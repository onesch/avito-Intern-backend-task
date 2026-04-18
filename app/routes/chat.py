from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.chat import ChatCreate, ChatResponse
from app.services.chat import create_chat, get_chats_by_user_id
from app.database.database import get_db


router = APIRouter(tags=["chats"])


@router.post(
    "/create-chat",
    response_model=ChatResponse,
    summary="Create a new chat",
    description="Creates a new chat in the database using provided name and users id list."
)
def create_chat_endpoint(
    chat: ChatCreate,
    db: Session = Depends(get_db),
):
    """
    Returns created chat object.

    - name: unique name for the chat
    - users: users id list
    """
    return create_chat(name=chat.name, users=chat.users, db=db)


@router.get(
    "/get-chats/user/{user_id}",
    response_model=List[ChatResponse],
    summary="Get user chats",
    description="Gets a list of Chat class objects using provided unique user id."
)
def get_chat_endpoint(
    user_id: int,
    db: Session = Depends(get_db),
):
    """
    Returns list of Chat class objects.

    - user_id: unique user id
    """
    return get_chats_by_user_id(user_id=user_id, db=db)
