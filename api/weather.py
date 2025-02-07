from fastapi import APIRouter, HTTPException
from services.weather_service import fetch_weather, get_bulk_location_weater
from schema.weather import WeatherResponse,BulkWeatherResponse,LocationData
from typing import List


router = APIRouter()

@router.post("/weather", response_model=WeatherResponse)
async def post_weather(city: str):
    data = await fetch_weather(city)
    if not data:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")

    return WeatherResponse(
        city=data["name"],
        temperature=data["main"]["temp"],
        description=data["weather"][0]["description"]
    )


@router.get("/bulk", response_model=BulkWeatherResponse)
async def get_bulk(city: str):
    data = await get_bulk_location_weater(city)

    if not data:
        raise HTTPException(status_code=404, detail="No se encontraron ubicaciones")

    locations = [LocationData(city=item["name"], local_names=item.get("local_names", {})) for item in data]

    return BulkWeatherResponse(locations=locations)