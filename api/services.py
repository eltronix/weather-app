import requests
import os
from statistics import mean, median


class WeatherService:

    @staticmethod
    def fetch_forecast(city, days):
        temps_collection = WeatherService._fetch_forecasts(city, days)

        computed_temps = {
            "maximum": round(max(temps_collection["max_temps"]), 1),
            "minimum": round(min(temps_collection["min_temps"]), 1),
            "average": round(mean(temps_collection["avg_temps"]), 1),
            "median": round(median([*temps_collection["max_temps"], *temps_collection["min_temps"], *temps_collection["avg_temps"]]), 1)
        }

        return computed_temps

    @staticmethod
    def _fetch_forecasts(city, days): # pragma: no cover
        key = os.environ.get('WEATHER_APP_API_KEY', "2eba2e3d66f34646bb7145246222610")
        url = f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={city}&days={days}&aqi=no&alerts=no"

        response = requests.get(url)

        if response.status_code != requests.codes.ok:
            response.raise_for_status() 

        json_response = response.json()
        forecasts = json_response.get("forecast").get("forecastday")

        temps_collection = {
            "max_temps": [],
            "min_temps": [],
            "avg_temps": []
        }

        for forecast in forecasts:
            temps_collection["max_temps"].append(forecast.get("day").get("maxtemp_c"))
            temps_collection["min_temps"].append(forecast.get("day").get("mintemp_c"))
            temps_collection["avg_temps"].append(forecast.get("day").get("avgtemp_c"))

        return temps_collection
