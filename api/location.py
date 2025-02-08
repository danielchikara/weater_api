
from fastapi import APIRouter, HTTPException
from services.weather_service import  get_location_service
from schema.weather import LocationWeatherResponse,LocationData

router = APIRouter()

@router.get("/location", response_model=LocationWeatherResponse)
async def get_location(city: str):
    data = await get_location_service(city)

    if not data:
        raise HTTPException(status_code=404, detail="No se encontraron ubicaciones")

    locations = [LocationData(city=item["name"], local_names=item.get("local_names", {})) for item in data]

    return LocationWeatherResponse(locations=locations)