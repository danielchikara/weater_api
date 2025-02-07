from pydantic import BaseModel
from typing import List, Dict


class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str


class LocationData(BaseModel):
    city: str
    local_names: Dict[str, str]


class BulkWeatherResponse(BaseModel):
    locations: List[LocationData]    
