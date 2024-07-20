import unittest
from app.weather_api import WeatherAPI

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.weather_api = WeatherAPI()

    def test_get_weather(self):
        response = self.weather_api.get_weather('Москва')
        self.assertIn('city_name', response)
        self.assertIn('data', response)

if __name__ == '__main__':
    unittest.main()
