from fastapi import FastAPI
from app.api.usuarios import router as usuarios_router
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging(settings.LOG_LEVEL)

app = FastAPI()
app.include_router(usuarios_router)


