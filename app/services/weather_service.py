from app.clients.weather_client import WeatherClient


class WeatherService:
    def __init__(self):
        self.weather_client = WeatherClient()

    async def get_weather(self, city: str):
        data = await self.weather_client.get_current_weather(city)

        return {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temperature": data["current"]["temp_c"],
            "humidity": data["current"]["humidity"],
            "wind_speed": data["current"]["wind_kph"],
            "description": data["current"]["condition"]["text"],
        }