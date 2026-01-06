from app.db import obter_conexao

def criar_usuario(nome: str):
    conn = obter_conexao()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO usuarios (nome) VALUES (%s) RETURNING id, nome",
        (nome,)
    )

    usuario = cur.fetchone()
    conn.commit()

    return {"id": usuario[0], "nome": usuario[1]}


def listar_usuarios():
    try:
        conn = obter_conexao()
        cur = conn.cursor()

        cur.execute("SELECT id, nome FROM usuarios")
        usuarios = cur.fetchall()

        return [{"id": u[0], "nome": u[1]} for u in usuarios]

    except Exception as e:
        print("ERRO REAL AO LISTAR:", repr(e))
        raise
