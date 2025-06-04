from unittest.mock import Mock
from src.services.irrigation_service import IrrigationService

def test_calculate_irrigation_time(mocker):
    # Mock the weather service response
    mock_weather_response = {
        "main": {"temp": 25.0, "humidity": 60},
        "weather": [{"description": "clear"}]
    }
    mocker.patch(
        "src.services.weather_service.requests.get",
        return_value=Mock(status_code=200, json=lambda: mock_weather_response)  
    )

    service = IrrigationService(weather_api_key="fake_key")
    result = service.calculate_irrigation_time(soil_moisture=0.5, city="TestCity", crop_type="Wheat")
    assert result == 60.0  # Check the stubbed result