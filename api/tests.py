# As the project grows we can convert this to a package

from django.test import SimpleTestCase
from rest_framework.test import APITestCase
from unittest.mock import Mock, patch
from .services import WeatherService

@patch("api.services.WeatherService.fetch_forecast")
class ForecastDetailGetTests(APITestCase):
    mock_data = {"maximum": 25, "minimum": 25, "average": 25, "median": 25}
    
    def test__it_passes_given_valid_params(self, mock_fetch_forecast: Mock):
        mock_fetch_forecast.return_value = self.mock_data

        response = self.client.get("/api/locations/london/?days=4")
        
        mock_fetch_forecast.assert_called()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.mock_data)
    
    def test_it_passes_with_missing_days_param(self, mock_fetch_forecast: Mock):
        mock_fetch_forecast.return_value = self.mock_data

        response = self.client.get("/api/locations/london/")
        
        mock_fetch_forecast.assert_called()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.mock_data)

    def test_it_fails_with_missing_city_param(self, mock_fetch_forecast: Mock):
        response = self.client.get("/api/locations/?days=4")
        
        self.assertEqual(response.status_code, 404)



class WeatherServiceTests(SimpleTestCase):
    @patch("api.services.WeatherService._fetch_forecasts")
    def test_it_passes_given_valid_params(self, mock_fetch_forecasts: Mock):

        mock_fetch_forecasts.return_value = {
            "max_temps": [20.9, 17.9, 21.1, 18.0],
            "min_temps": [14.3, 13.3, 12.8, 14.1],
            "avg_temps": [17.1, 16.2, 16.6, 15.6],
        }

        city = "London"
        days = 4

        response = WeatherService.fetch_forecast(city, days)
        self.assertEqual(
            response,
            {'maximum': 21.1, 'minimum': 12.8, 'average': 16.4, 'median': 16.4},
        )
        mock_fetch_forecasts.assert_called()
        mock_fetch_forecasts.assert_called_with(city, days)
