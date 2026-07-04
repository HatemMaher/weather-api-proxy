import httpx
from fastapi import HTTPException

from app.core.config import settings


class WeatherClient:
    async def get_current_weather(self, city: str) -> dict:
        url = f"{settings.weather_base_url}/current.json"

        params = {
            "key": settings.weather_api_key,
            "q": city,
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, params=params)

                response.raise_for_status()

                return response.json()

            except httpx.HTTPStatusError:
                if response.status_code == 400:
                    raise HTTPException(
                        status_code=404,
                        detail=f"City '{city}' not found."
                    )

                if response.status_code == 401:
                    raise HTTPException(
                        status_code=401,
                        detail="Invalid Weather API key."
                    )

                raise HTTPException(
                    status_code=503,
                    detail="Weather service is unavailable."
                )

            except httpx.RequestError:
                raise HTTPException(
                    status_code=503,
                    detail="Unable to connect to Weather API."
                )