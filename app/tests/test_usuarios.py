from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

def test_erro_ao_criar_usuario():
    with patch("app.api.usuarios.criar_usuario") as mock_criar:
        mock_criar.side_effect = Exception("Banco indisponível")

        response = client.post("/usuarios", json={"nome": "João"})

        assert response.status_code == 500

def test_erro_ao_listar_usuarios():
    with patch("app.api.usuarios.listar_usuarios") as mock_listar:
        mock_listar.side_effect = Exception("Falha no banco")

        response = client.get("/usuarios")

        assert response.status_code == 500
