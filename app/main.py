from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database.init_db import init_db

from app.routes.user import router as user_api_router
from app.routes.chat import router as chat_api_router
from app.routes.message import router as message_api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Service lifespan manager.

    Runs startup logic such as database initialization
    before the app starts serving requests.
    """
    init_db()
    yield


def create_app() -> FastAPI:
    """
    Function for FastAPI app.

    Returns:
        FastAPI: Configured FastAPI app instance with routers and lifespan.
    """
    app = FastAPI(lifespan=lifespan)

    # routers
    app.include_router(user_api_router, prefix="/users")
    app.include_router(chat_api_router, prefix="/chats")
    app.include_router(message_api_router, prefix="/messages")

    return app


app = create_app()
