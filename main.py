from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = FastAPI(
    title="FastAPI Application",
    description="Aplicación FastAPI con variables de entorno",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "¡Bienvenido a FastAPI!",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}

