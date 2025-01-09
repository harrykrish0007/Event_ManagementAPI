from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_event():
    response = client.post("/events/", json={
        "name": "Test Event",
        "description": "A test event",
        "start_time": "2023-01-01T10:00:00",
        "end_time": "2023-01-01T12:00:00",
        "location": "Test Location",
        "max_attendees": 100
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Event"