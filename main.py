from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from Controllers.MeditionController import medition

# se puede cargar cualquier variable de entorno necesaria
load_dotenv()

# Se carga la aplicacion de FastAPI, esta tiene la ventaja de tener openapi o Swagger ya implementado
# ya que es de los mismos creadores. Si se quieren ver las rutas ir al localhost:8000/docs o {base-url}/docs
app = FastAPI(
    title="Medition CRUD",
    description="CRUD for meditions with Mongo data base",
    version="0.0.1",
)

# Se crea middleware para evitar problemas del CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Se incluyen las rutas de las mediciones
app.include_router(medition)
