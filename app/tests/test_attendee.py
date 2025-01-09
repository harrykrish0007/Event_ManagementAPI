from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_attendee():
    response = client.post("/attendees/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone_number": "1234567890",
        "event_id": 1
    })
    assert response.status_code == 200
    assert response.json()["email"] == "john@example.com"