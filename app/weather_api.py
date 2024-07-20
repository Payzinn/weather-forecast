import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherAPI:
    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.base_url = 'https://api.weatherbit.io/v2.0/forecast/daily'

    def get_weather(self, city):
        url = f'{self.base_url}?city={city}&key={self.api_key}&lang=ru&days=10'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'Ошибка': f'Ошибка получения данных: {response.status_code}'}
