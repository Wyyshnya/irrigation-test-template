import requests


class WeatherService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str) -> dict:
        params = {"q": city, "appid": self.api_key}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()
