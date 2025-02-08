from fastapi import FastAPI
from api.weather import router as weather_router
from api.location import router as location_router

tags_metadata = [
    {
        " name ": " weather",
        " description ": " endpoint para consulta del clima de la ciudad "
    },
    {
        " name ": " location ",
        " description ": " este endpoint te permite consultar los nombres de la ciudad en diferentes paises ",
        
    },
]

app = FastAPI()

app.include_router(weather_router, prefix="/api", tags=["weather"])
app.include_router(location_router, prefix="/api", tags=["location"])

@app.get("/")
def home():
    return {"message": "API de Clima con FastAPI"}