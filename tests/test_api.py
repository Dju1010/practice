import pytest
from app import create_app
from models import db


@pytest.fixture
def client(tmp_path):
    db_path = f"sqlite:///{tmp_path}/test.db"
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["TESTING"] = True

    with app.app_context():
        db.drop_all()
        db.create_all()

    with app.test_client() as c:
        yield c


def test_list_empty(client):
    r = client.get("/notes")
    assert r.status_code == 200
    assert r.get_json() == []


def test_create_note(client):
    r = client.post("/notes", json={"title": "Test", "body": "Hello"})
    assert r.status_code == 201
    data = r.get_json()
    assert data["title"] == "Test"
    assert data["body"] == "Hello"
    assert "id" in data


def test_get_note(client):
    r = client.post("/notes", json={"title": "One"})
    nid = r.get_json()["id"]

    r = client.get(f"/notes/{nid}")
    assert r.status_code == 200
    assert r.get_json()["title"] == "One"


def test_update_note(client):
    r = client.post("/notes", json={"title": "Old"})
    nid = r.get_json()["id"]

    r = client.put(f"/notes/{nid}", json={"title": "New"})
    assert r.status_code == 200
    assert r.get_json()["title"] == "New"


def test_delete_note(client):
    r = client.post("/notes", json={"title": "To delete"})
    nid = r.get_json()["id"]

    r = client.delete(f"/notes/{nid}")
    assert r.status_code == 204

    r = client.get(f"/notes/{nid}")
    assert r.status_code == 404


def test_get_missing(client):
    r = client.get("/notes/9999")
    assert r.status_code == 404