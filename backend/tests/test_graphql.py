import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from app.main import app


@pytest.mark.asyncio
async def test_users_query():
    query = """
    query {
        users {
            id
            name
            email
        }
    }
    """
    with TestClient(app) as test_client:
        async with AsyncClient(app=test_client.app, base_url="http://test") as client:
            response = await client.post("/graphql", json={"query": query})

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "users" in data["data"]
    assert len(data["data"]["users"]) == 2
    assert data["data"]["users"][0]["name"] == "John Doe"
    assert data["data"]["users"][1]["email"] == "jane@example.com"
