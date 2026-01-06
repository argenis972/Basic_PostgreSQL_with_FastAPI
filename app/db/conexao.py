from app.core.config import DB_CONFIG
import psycopg2

def obter_conexao():
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        dbname=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        port=DB_CONFIG["port"],
    )

