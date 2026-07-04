from pydantic import BaseModel


class WeatherResponse(BaseModel):
    city: str
    country: str
    temperature: float
    humidity: int
    wind_speed: float
    description: str