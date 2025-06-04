import requests


class SoilService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://example-soil-api.com/data"

    def get_soil_data(self, location: str) -> dict:
        params = {"location": location, "key": self.api_key}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()
