# API Weather

**Website:**  


# 🌦️ FastAPI Weather API  

API para obtener información meteorológica usando FastAPI y OpenWeather.

---

## 📂 Estructura del Proyecto  

La estructura del proyecto que determine fue la siguiente

```bash
fastapi_weather/
│── app/
│   ├── api/
│   │   ├── weather.py      # Endpoint para obtener el clima
│   │   ├── location.py     # Endpoint para obtener ubicaciones
│   │   ├── __init__.py
│   ├── core/
│   │   ├── config.py           # Configuración y variables de entorno
│   │   ├── __init__.py
│   ├── services/
│   │   ├── weather_service.py  # Lógica para consultar clima
│   │   ├── __init__.py
│   ├── main.py                 # Punto de entrada de la API
│   ├── models/
│   ├── schemas/
│   │   ├── weather.py          # Esquema de respuesta del clima
│   │   ├── __init__.py
│   ├── __init__.py
│── requirements.txt            # Dependencias del proyecto
│── README.md                   # Documentación

```


## En la terminal 
Instalación de requerimientos  con su entorno virtual de preferencia  
```
pip  install -r  requirements.txt  
```
Para iniciar la plicación  
```
uvicorn main:app --reload  
```

