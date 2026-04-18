from app.database.database import engine
from app.models.base import Base
from app.settings import REFRESH_DB

# Register models with Base.metadata
from app.models.user import User
from app.models.chat import Chat
from app.models.associations import chat_user_association

def init_db():
    """
    Initialize database function.

    Creates all tables defined in SQLAlchemy Base metadata.
    This function should be called on application startup.
    """
    if REFRESH_DB:
        Base.metadata.create_all(bind=engine)
