from fastapi.testclient import TestClient

from src.db import get_engine, get_session
from src.main import app
from src.models import Base, Account


client = TestClient(app)


def setup_module():
    Base.metadata.create_all(get_engine())

    # create mock user
    _session = get_session()
    _session.add(Account(id="123321", username="test", password="abcd1234"))
    _session.commit()
    _session.close()


def teardown_module():
    Base.metadata.drop_all(get_engine())


def test_success_signin():
    # incorrect password
    resp = client.post(
        "signin",
        json={"username": "test", "password": "abcd1234"},
    )
    assert resp.status_code == 200
    assert resp.json()["msg"] == "success"


def test_fail_signin():
    # user not found
    resp = client.post(
        "signin",
        json={"username": "123321", "password": "123321"},
    )
    assert resp.status_code == 401
    assert resp.json()["msg"] == "user not found"

    # incorrect password
    resp = client.post(
        "signin",
        json={"username": "test", "password": "123321"},
    )
    assert resp.status_code == 401
    assert resp.json()["msg"] == "incorrect password"
