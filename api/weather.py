from fastapi import APIRouter, HTTPException
from services.weather_service import fetch_weather
from schema.weather import WeatherResponse,LocationWeatherResponse,LocationData


router = APIRouter()
#buscar ciudad 
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

