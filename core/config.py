from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = "a881ac3b4b68c403493ef871e66c5401"
    BASE_URL: str = "https://api.openweathermap.org/data/2.5/weather"
    BULK_URL: str = "http://api.openweathermap.org/geo/1.0/direct"



settings = Settings()