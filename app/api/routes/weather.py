from typing import Annotated

from fastapi import APIRouter, Query

from app.core.config import settings
from app.schemas.common import HealthResponse
from app.schemas.weather import WeatherResponse
from app.services.weather_service import WeatherService

router = APIRouter()

weather_service = WeatherService()


@router.get(
    "/",
    response_model=HealthResponse,
    tags=["Health"],
    summary="Health Check",
    description="Checks whether the Weather API Proxy service is running.",
)
async def health_check():
    return HealthResponse(
        status="healthy",
        service=settings.app_name,
        version="1.0.0",
    )


@router.get(
    "/weather",
    response_model=WeatherResponse,
    tags=["Weather"],
    summary="Get Current Weather",
    description="Retrieves the current weather information for the specified city.",
    responses={
        200: {"description": "Weather retrieved successfully."},
        404: {"description": "City not found."},
        401: {"description": "Invalid API key."},
        503: {"description": "Weather service unavailable."},
    },
)
async def get_weather(
    city: Annotated[
        str,
        Query(
            ...,
            min_length=2,
            max_length=50,
            description="Name of the city (e.g. Cairo, London, Paris)",
            examples=["Cairo"],
        ),
    ]
):
    return await weather_service.get_weather(city)