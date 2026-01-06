from unittest.mock import patch

def test_criar_usuario_sucesso(client):
    usuario_falso = {
        "id": 1,
        "nome": "João"
    }

    with patch("app.api.usuarios.criar_usuario") as mock_criar:
        mock_criar.return_value = usuario_falso

        response = client.post("/usuarios", json={"nome": "João"})

        assert response.status_code == 201
        assert response.json() == usuario_falso


