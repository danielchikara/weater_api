from fastapi import FastAPI
from api.weather import router as weather_router

app = FastAPI()

app.include_router(weather_router, prefix="/api", tags=["weather"])

@app.get("/")
def home():
    return {"message": "API de Clima con FastAPI"}