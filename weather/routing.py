from django.urls import re_path
from .consumers import WeatherConsumer

websocket_urlpatterns = [
    re_path(r'ws/weather/$', WeatherConsumer.as_asgi()),
]
