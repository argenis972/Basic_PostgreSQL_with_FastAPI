from fastapi import APIRouter, HTTPException
from app.services.usuarios import criar_usuario, listar_usuarios
from app.schemas.usuarios import UsuarioCriar

router = APIRouter()

@router.post("/usuarios", status_code=201)
def criar(usuario: UsuarioCriar):
    try:
        return criar_usuario(usuario.nome)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/usuarios")
def listar():
    try:
        return listar_usuarios()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))