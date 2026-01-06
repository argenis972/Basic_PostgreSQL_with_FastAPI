from pydantic import BaseModel


class UsuarioCriar(BaseModel):
    nome: str


class UsuarioOut(BaseModel):
    id: int
    nome: str

