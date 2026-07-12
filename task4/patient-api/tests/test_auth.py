def test_register_user(client):
    response = client.post("/auth/register", json={"username": "alice", "password": "secret123"})
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "alice"
    assert "id" in data


def test_register_duplicate_username(client):
    client.post("/auth/register", json={"username": "bob", "password": "secret123"})
    response = client.post("/auth/register", json={"username": "bob", "password": "different"})
    assert response.status_code == 409


def test_login_success(client):
    client.post("/auth/register", json={"username": "carol", "password": "secret123"})
    response = client.post("/auth/token", data={"username": "carol", "password": "secret123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post("/auth/register", json={"username": "dave", "password": "secret123"})
    response = client.post("/auth/token", data={"username": "dave", "password": "wrongpass"})
    assert response.status_code == 401


def test_login_nonexistent_user(client):
    response = client.post("/auth/token", data={"username": "ghost", "password": "whatever"})
    assert response.status_code == 401