from typing import Dict
from django.utils.translation import ugettext_lazy as _


class WeatherParser:
    WIND_METRICS = {
        "standard": 'm/s',
        "metric": 'm/s',
        "imperial": 'mph'
    }
    TEMP_METRICS = {
        "standard": "K",
        "metric": "C",
        "imperial": "F"
    }
    RU_TRANSLATIONS = {
        "m/s": "м/c",
        "mph": "мили/час",
        "F": "Ф",
        "K": "К",
        "C": "Ц",
        "north": "северный",
        "east": "южный",
        "south": "восточный",
        "west": "западный",
        "mm Hg": "рт. ст."
    }

    """get raw dict return needed dict"""
    @classmethod
    def get_params(cls, raw_dict: Dict, units: str, lang: str) -> Dict:
        if type(raw_dict) != dict:
            return {"message": _("Something went wrong")}

        params = {
            "city": raw_dict.get("name", _("Not found")),
            "temp": cls._get_temp(raw_dict, units, lang),
            "description": cls._get_description(raw_dict),
            "wind_speed": cls._get_wind_speed(raw_dict, units, lang),
            "wind_deg": cls._get_wind_deg(raw_dict, units, lang),
            "humidity": cls._get_humidity(raw_dict),
            "pressure": cls._get_pressure(raw_dict, units, lang),
            "rain": cls._get_rain(raw_dict),
            "ico": cls._get_ico(raw_dict)
        }

        return params

    @classmethod
    def _get_wind_speed(cls, raw_dict, units, lang):
        if raw_dict.get('wind'):
            wind_speed = int(raw_dict['wind'].get('speed', 0))
            metric = cls.WIND_METRICS[units]
            if lang == 'ru':
                metric = cls.RU_TRANSLATIONS[metric]

            return f"{wind_speed} {metric}"
        return "Not found"

    @classmethod
    def _get_temp(cls, raw_dict, units, lang):
        if raw_dict.get('main'):
            temperature = int(raw_dict['main'].get('temp', 0))
            metric = cls.TEMP_METRICS[units]
            if lang == 'ru':
                metric = cls.RU_TRANSLATIONS[metric]
            return f"{temperature} {metric}"
        return "Not found"

    @classmethod
    def _get_wind_deg(cls, raw_dict, units, lang):
        NORTH = 0
        EAST = 90
        SOUTH = 180
        WEST = 270
        if raw_dict.get('wind'):
            wind_deg = raw_dict['wind'].get('deg', 0)
            if NORTH <= wind_deg < EAST:
                direction = 'north'
            elif EAST <= wind_deg < SOUTH:
                direction = 'east'
            elif SOUTH <= wind_deg < WEST:
                direction = 'south'
            else:
                direction = 'west'

            if lang == 'ru':
                direction = cls.RU_TRANSLATIONS[direction]
            return direction
        return "Not found"

    @classmethod
    def _get_humidity(cls, raw_dict):
        if raw_dict.get('main'):
            return raw_dict['main'].get('humidity', 'not found')
        return "not found"

    @classmethod
    def _get_pressure(cls, raw_dict, units, lang):
        if raw_dict.get('main'):
            pressure = raw_dict['main'].get('pressure', 'not found')
            metric = 'mm Hg'
            if lang == 'ru':
                metric = cls.RU_TRANSLATIONS[metric]
            return f"{pressure} {metric}"
        return "not found"

    @classmethod
    def _get_rain(cls, raw_dict):
        if raw_dict.get('rain'):
            return f"{raw_dict['rain'].get('1h')} %"
        return "not found"

    @classmethod
    def _get_ico(cls, raw_dict):
        if raw_dict.get('weather') and type(raw_dict['weather'][0]) == dict:
            return raw_dict['weather'][0].get('icon')
        return 'default icon'

    @classmethod
    def _get_description(cls, raw_dict):
        if raw_dict.get('weather') and type(raw_dict['weather'][0]) == dict:
            return raw_dict['weather'][0].get('description')
        return 'not found'
