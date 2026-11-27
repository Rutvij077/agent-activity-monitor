
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_agent_run_endpoint():
    response = client.post(
        "/agent/run",
        json={"input_text": "Explain machine learning"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "completed"
    assert data["execution_id"]
