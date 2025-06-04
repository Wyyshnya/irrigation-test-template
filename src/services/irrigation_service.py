from src.services.weather_service import WeatherService


class IrrigationService:
    def __init__(self, weather_api_key: str):
        self.weather_service = WeatherService(api_key=weather_api_key)

    def calculate_irrigation_time(
        self, soil_moisture: float, city: str, crop_type: str
    ) -> float:
        weather_data = self.weather_service.get_weather(city)
        # Логика расчёта времени полива на основе погоды, влажности почвы и типа культуры
        return 60.0  # Пример результата в минутах
