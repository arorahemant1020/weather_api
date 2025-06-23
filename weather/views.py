from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_weather_data

@api_view(['GET'])
def current_weather(request, city):
    data = get_weather_data(city)
    if data:
        return Response({
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        })
    return Response({'error': 'City not found'}, status=404)
