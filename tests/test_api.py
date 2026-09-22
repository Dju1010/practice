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

def test_create_with_tags(client):
    r = client.post("/notes", json={
        "title": "With tags",
        "tags": ["work", "urgent"]
    })
    assert r.status_code == 201
    data = r.get_json()
    assert "work" in data["tags"]
    assert "urgent" in data["tags"]


def test_pagination(client):
    for i in range(15):
        client.post("/notes", json={"title": f"Note {i}"})

    r = client.get("/notes?page=1&size=5")
    data = r.get_json()
    assert data["total"] == 15
    assert data["page"] == 1
    assert data["size"] == 5
    assert len(data["items"]) == 5

    r = client.get("/notes?page=3&size=5")
    data = r.get_json()
    assert len(data["items"]) == 5


def test_search(client):
    client.post("/notes", json={"title": "Buy bread"})
    client.post("/notes", json={"title": "Buy milk"})
    client.post("/notes", json={"title": "Read book"})

    r = client.get("/notes?search=Buy")
    data = r.get_json()
    assert data["total"] == 2


def test_list_empty(client):
    r = client.get("/notes")
    assert r.status_code == 200
    data = r.get_json()
    assert data["items"] == []
    assert data["total"] == 0