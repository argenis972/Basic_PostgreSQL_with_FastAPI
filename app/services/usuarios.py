import logging
from app.db.pool import pool

logger = logging.getLogger(__name__)

def criar_usuario(nome: str):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO usuarios (nome) VALUES (%s) RETURNING id, nome",
                (nome,),
            )
            usuario = cur.fetchone()
            conn.commit()

    return {"id": usuario[0], "nome": usuario[1]}


def listar_usuarios():
    try:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, nome FROM usuarios")
                usuarios = cur.fetchall()

        return [{"id": u[0], "nome": u[1]} for u in usuarios]
    except Exception:
        logger.exception("Erro ao listar usuários")
        raise