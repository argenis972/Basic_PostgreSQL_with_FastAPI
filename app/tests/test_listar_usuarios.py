from unittest.mock import patch

def test_listar_usuarios(client):
    usuarios_falsos = [
        {"id": 1, "nome": "Ana"},
        {"id": 2, "nome": "Carlos"},
    ]

    with patch("app.api.usuarios.listar_usuarios") as mock_listar:
        mock_listar.return_value = usuarios_falsos

        response = client.get("/usuarios")

        assert response.status_code == 200
        assert response.json() == usuarios_falsos