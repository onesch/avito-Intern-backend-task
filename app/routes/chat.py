from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.chat import ChatCreate, ChatResponse
from app.services.chat import create_chat
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
