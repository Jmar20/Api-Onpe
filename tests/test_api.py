from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_happy_path():
    payload = {
        "dni": "12345678",
        "fecha_emision": "2015-03-10",
        "digito_verificador": "6"
    }
    r = client.post("/api/consulta", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["nombres"] == "Juan Carlos"
    assert data["es_miembro_mesa"] is True
    assert "lugar_votacion" in data


def test_invalid_digito():
    payload = {
        "dni": "12345678",
        "fecha_emision": "2015-03-10",
        "digito_verificador": "0"
    }
    r = client.post("/api/consulta", json=payload)
    assert r.status_code == 400


def test_not_found():
    payload = {
        "dni": "12345678",
        "fecha_emision": "2020-01-01",
        "digito_verificador": "6"
    }
    r = client.post("/api/consulta", json=payload)
    assert r.status_code == 404
