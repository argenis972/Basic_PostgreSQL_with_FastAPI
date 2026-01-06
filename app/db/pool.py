from psycopg_pool import ConnectionPool
from app.core.config import settings

pool = ConnectionPool(conninfo=settings.DATABASE_URL, open=True)