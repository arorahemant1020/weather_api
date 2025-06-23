import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .utils import get_weather_data

class WeatherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        city = data.get('city')
        weather = get_weather_data(city)
        if weather:
            await self.send(text_data=json.dumps({
                'city': weather['name'],
                'temperature': weather['main']['temp'],
                'humidity': weather['main']['humidity'],
                'description': weather['weather'][0]['description']
            }))
        else:
            await self.send(text_data=json.dumps({'error': 'City not found'}))
