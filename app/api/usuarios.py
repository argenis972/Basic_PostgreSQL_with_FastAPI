from fastapi import APIRouter, HTTPException
from app.schemas.usuarios import UsuarioCriar, UsuarioOut
from app.services.usuarios import criar_usuario, listar_usuarios

router = APIRouter()

@router.post("/usuarios", status_code=201, response_model=UsuarioOut)
def criar(usuario: UsuarioCriar):
    # Cria um novo usuário com o nome fornecido.
    try:
        return criar_usuario(usuario.nome)
    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao criar usuário")


@router.get("/usuarios", response_model=list[UsuarioOut])
def listar():
    # Lista todos os usuários existentes.
    try:
        return listar_usuarios()
    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao listar usuários")