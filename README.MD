# API Weather

### Primero que todo muchas gracias por la oportunidad  me diverti con la prueba la hice con Fast Api para ir aprendiendo mejor, esta prueba me permitio mejorar en muchos aspectos pese que mi dominio fuerte es django, siento que pude hacerla muy bien quedo al pendiente  para retroalimentación muchas gracias

**Website:**  https://weather-api-fbpi.onrender.com/docs
Aveces se demora en abrir por que es un servidor gratuito pero desde ahi pueden probar los endpoints  desplegando y pulsando el boton Try it out

Existen 2 ramas una main y otra de deploy sugiero usar main 

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

## Parte B de la prueba 
para ejecutar el script hay que crear una base de datos  y una tabla que se llame leads
dependiendo del sistema operativo debes instalar psycopg2  o si es linux puedes usar el que esta en los requirements despues de eso ejecutar    

```
CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    budget INT
);
```

```
python3 leads.py  
```

##  Parte  C

Si es de forma manual le pediria a chatgpt de  

```
" mejorar el siguiente Prompt  generar un correo amable  para un lead de nombre Ana  que esta ubicado en la ciudad de medellin con un presupuesto de 200 millones", puedes hacerme las preguntas que necesites para la mejora de este "
```
me genero el siguiente texto

```
Genera un correo formal y amable para un lead llamado Ana, ubicado en Medellín, con un presupuesto de 200 millones de pesos colombianos. Ana es un contacto frío interesado en el sector de la construcción. El objetivo del correo es presentarle una propuesta y saber si necesita más información.
```
me genero el siguiente prompt https://chatgpt.com/share/67a6f897-e71c-8010-b193-e6c0157c093f

```
Asunto: Propuesta para su proyecto en el sector construcción

Estimada Ana,

Espero que este correo le encuentre bien. Mi nombre es Brandon Ortega y me especializo en soluciones para el sector de la construcción. Me gustaría compartir con usted una propuesta alineada a su presupuesto de 200 millones de pesos y diseñada para maximizar el valor de su inversión.

Si está interesada, con gusto le brindaré más detalles y resolveré cualquier inquietud que tenga. ¿Le gustaría que agendemos una reunión o le envíe información más detallada?

Quedo atento a su respuesta.

Saludos cordiales,
Brandon Ortega
[Tu contacto]
```
he de decir que no me pidio nombre de contacto por que chatgpt a ido aprendiedo de mi usuario muchas cosas