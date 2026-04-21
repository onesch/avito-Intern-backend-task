from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.message import MessageCreate, MessageResponse
from app.services.message import create_message, get_messages_by_chat_id


router = APIRouter(tags=["messages"])


@router.post(
    "/create-message",
    response_model=MessageResponse,
    summary="Create a new chat",
    description="Creates a new message in the database using provided chat_id, author_id and text."
)
def create_message_endpoint(
    message: MessageCreate,
    db: Session = Depends(get_db),
):
    """
    Returns created message object.

    - chat_id: unique chat id
    - author_id: unique user id
    - text: text of the message
    """
    return create_message(
        chat_id=message.chat_id,
        author_id=message.author_id,
        text=message.text,
        db=db,
    )


@router.get(
    "/get-messages/chat/{chat_id}",
    response_model=List[MessageResponse],
    summary="Get chat messages",
    description="Gets a list of Chat messages objects using provided unique chat id."
)
def get_message_endpoint(
    chat_id: int,
    db: Session = Depends(get_db),
):
    """
    Returns list of Chat messages objects.

    - chat_id: unique chat id
    """
    return get_messages_by_chat_id(chat_id=chat_id, db=db)
