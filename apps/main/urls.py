from apps.main import converters
from django.urls import path, register_converter

from apps.main import views
register_converter(converters.SlugOrNotConverter, 'slug_or_not')

urlpatterns = (
    path('', views.home, name='home'),
    path('weather', views.WeatherView.as_view(), name="weather")
)

app_name = 'main'
