from app.database.database import engine
from app.models.base import Base
from app.settings import REFRESH_DB


def init_db():
    """
    Initialize database function.

    Creates all tables defined in SQLAlchemy Base metadata.
    This function should be called on application startup.
    In production, use Alembic migrations instead.
    """
    if REFRESH_DB:
        Base.metadata.create_all(bind=engine)
