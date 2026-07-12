from app.auth import create_access_token

def auth_headers(client):
    client.post("/auth/register", json={"username": "tester", "password": "secret123"})
    response = client.post("/auth/token", data={"username": "tester", "password": "secret123"})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def make_patient(client, **overrides):
    payload = {
        "name": "John Doe",
        "age": 40,
        "condition": "Diabetes",
        "risk_score": 50,
        "active": True,
    }
    payload.update(overrides)
    return client.post("/patients/", json=payload, headers=auth_headers(client))


def test_create_patient(client):
    response = make_patient(client)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert "id" in data


def test_create_patient_requires_auth(client):
    payload = {"name": "Jane", "age": 30, "condition": "Asthma", "risk_score": 20}
    response = client.post("/patients/", json=payload)
    assert response.status_code == 401


def test_create_patient_validation_error(client):
    response = client.post(
        "/patients/",
        json={"name": "Bad", "age": 200, "condition": "X", "risk_score": 10},
        headers=auth_headers(client),
    )
    assert response.status_code == 422


def test_get_patients_list(client):
    make_patient(client)
    response = client.get("/patients/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


def test_get_patients_filter_active(client):
    make_patient(client, name="Active Pat", active=True)
    make_patient(client, name="Inactive Pat", active=False)
    response = client.get("/patients/?active=false")
    assert response.status_code == 200
    assert all(p["active"] is False for p in response.json())


def test_get_patients_filter_condition(client):
    make_patient(client, condition="Hypertension")
    response = client.get("/patients/?condition=Hypertension")
    assert response.status_code == 200
    assert all(p["condition"] == "Hypertension" for p in response.json())


def test_get_single_patient(client):
    created = make_patient(client).json()
    response = client.get(f"/patients/{created['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_get_single_patient_not_found(client):
    response = client.get("/patients/9999")
    assert response.status_code == 404


def test_update_patient_put(client):
    created = make_patient(client).json()
    payload = {"name": "Updated Name", "age": 50, "condition": "Flu", "risk_score": 30, "active": True}
    response = client.put(f"/patients/{created['id']}", json=payload, headers=auth_headers(client))
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"


def test_update_patient_put_not_found(client):
    payload = {"name": "Ghost", "age": 50, "condition": "Flu", "risk_score": 30, "active": True}
    response = client.put("/patients/9999", json=payload, headers=auth_headers(client))
    assert response.status_code == 404


def test_update_patient_put_requires_auth(client):
    created = make_patient(client).json()
    payload = {"name": "NoAuth", "age": 50, "condition": "Flu", "risk_score": 30, "active": True}
    response = client.put(f"/patients/{created['id']}", json=payload)
    assert response.status_code == 401


def test_patch_patient(client):
    created = make_patient(client).json()
    response = client.patch(
        f"/patients/{created['id']}", json={"risk_score": 99}, headers=auth_headers(client)
    )
    assert response.status_code == 200
    assert response.json()["risk_score"] == 99
    assert response.json()["name"] == created["name"]


def test_patch_patient_not_found(client):
    response = client.patch("/patients/9999", json={"risk_score": 99}, headers=auth_headers(client))
    assert response.status_code == 404


def test_patch_patient_requires_auth(client):
    created = make_patient(client).json()
    response = client.patch(f"/patients/{created['id']}", json={"risk_score": 99})
    assert response.status_code == 401


def test_delete_patient(client):
    created = make_patient(client).json()
    response = client.delete(f"/patients/{created['id']}", headers=auth_headers(client))
    assert response.status_code == 204

    follow_up = client.get(f"/patients/{created['id']}")
    assert follow_up.status_code == 404


def test_delete_patient_not_found(client):
    response = client.delete("/patients/9999", headers=auth_headers(client))
    assert response.status_code == 404


def test_delete_patient_requires_auth(client):
    created = make_patient(client).json()
    response = client.delete(f"/patients/{created['id']}")
    assert response.status_code == 401

def test_protected_route_invalid_token(client):
    response = client.post(
        "/patients/",
        json={"name": "X", "age": 30, "condition": "Y", "risk_score": 10},
        headers={"Authorization": "Bearer not-a-real-token"},
    )
    assert response.status_code == 401


def test_protected_route_token_for_missing_user(client):
    fake_token = create_access_token({"sub": "ghost_user_that_doesnt_exist"})
    response = client.post(
        "/patients/",
        json={"name": "X", "age": 30, "condition": "Y", "risk_score": 10},
        headers={"Authorization": f"Bearer {fake_token}"},
    )
    assert response.status_code == 401