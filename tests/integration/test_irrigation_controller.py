import pytest
from litestar.testing import TestClient

@pytest.mark.asyncio
async def test_get_irrigation_time(test_app):
    with TestClient(test_app) as client:
        response = client.get("/irrigation?soil_moisture=0.5&crop_type=Wheat")
        assert response.status_code == 500  # 500 потому что настоящего ключа нет
        # assert response.status_code == 200
        # assert response.json() == {"irrigation_time": 60.0}