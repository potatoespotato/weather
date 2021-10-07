from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from apps.main.busines_servises.openweathermap_api import ApiHelper


class WeatherView(View):

    def get(self, request):
        city_name = request.GET.get('city')
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        lang = request.GET.get('lang')
        units = request.GET.get('units')

        params = ApiHelper.get_weather(city_name, lat, lon, units=units, lang=lang)
        return JsonResponse(params)


def home(request):
    return render(request, 'main/pages/home.html')


def handler404(request, exception=None):
    return render(request, 'main/404.html', status=404)


def handler500(request, exception=None):
    return render(request, 'main/500.html', status=500)
