from typing import Dict
import requests
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from apps.main.busines_servises.weather_parser import WeatherParser


class ApiHelper:
    API_KEY = settings.API_KEY
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    UNITS_LIST = [
        "standard",
        "metric",
        "imperial"
    ]
    SMALL_LANG_LIST = [
        "ru",
        "en"
    ]

    @classmethod
    def get_weather_by_city_name(cls, city_name: str, units: str, lang: str) -> Dict:
        response = requests.get(f"{cls.BASE_URL}?q={city_name}&units={units}&appid={cls.API_KEY}&lang={lang}")
        if response.status_code == 200:
            return WeatherParser.get_params(response.json(), units, lang)
        return {"message": _("Something went wrong")}

    @classmethod
    def get_weather_by_lat_and_lon(cls, lat: str, lon: str, units: str, lang: str) -> Dict:
        response = requests.get(f"{cls.BASE_URL}?lat={lat}&lon={lon}&units={units}&appid={cls.API_KEY}&lang={lang}")
        if response.status_code == 200:
            return WeatherParser.get_params(response.json(), units, lang)
        return {"message": _("Something went wrong")}

    @classmethod
    def get_weather(cls, city_name=None, lat=None, lon=None, units="metric", lang="ru"):
        if units not in cls.UNITS_LIST:
            units = cls.UNITS_LIST[0]
        if lang not in cls.SMALL_LANG_LIST:
            lang = cls.SMALL_LANG_LIST[0]

        if city_name:
            return cls.get_weather_by_city_name(city_name, units=units, lang=lang)
        
        if lat and lon:
            return cls.get_weather_by_lat_and_lon(lat, lon, units=units, lang=lang)

        return {"message": _("Search params not found")}
