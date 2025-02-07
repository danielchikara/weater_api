import httpx
from core.config import settings

async def fetch_weather(city: str):
    params = {
        "q": city,
        "appid": settings.API_KEY,
        "units": "metric",
        "lang": "es"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.BASE_URL, params=params)

    if response.status_code != 200:
        return None

    return response.json()

async def get_bulk_location_weater(city: str):
    params = {
        "q": city,
        "appid": settings.API_KEY

    }
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.BULK_URL, params=params)

    if response.status_code != 200:
        return None

    return response.json()