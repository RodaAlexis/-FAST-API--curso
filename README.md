# FastAPI Application

Aplicación FastAPI con configuración mediante variables de entorno.

## 🚀 Inicio Rápido

### Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

2. Configurar las variables de entorno:
   - El archivo `.env` ya está creado con valores de ejemplo
   - Edita `.env` según tus necesidades

3. Ejecutar el servidor:
```bash
uvicorn main:app --reload
```

### Acceso

- **API**: http://localhost:8000
- **Documentación interactiva (Swagger)**: http://localhost:8000/docs
- **Documentación alternativa (ReDoc)**: http://localhost:8000/redoc

## 📋 Estructura del Proyecto

```
.
├── main.py              # Aplicación principal FastAPI
├── requirements.txt     # Dependencias del proyecto
├── .env                 # Variables de entorno (no versionado)
└── .gitignore          # Archivos ignorados por Git
```

## 🔧 Configuración

Las variables de entorno se configuran en el archivo `.env`. Algunas variables disponibles:

- `APP_NAME`: Nombre de la aplicación
- `APP_VERSION`: Versión de la aplicación
- `DEBUG`: Modo debug (True/False)
- `HOST`: Host del servidor
- `PORT`: Puerto del servidor

## 📚 Documentación

### Pydantic y FastAPI

Hola, a todas y a todos.

En esta sección se tratarán los siguientes temas:

- ¿Qué es Pydantic y por qué lo usa FastAPI?
- Pydantic
- Modelos básicos con Pydantic
- Validaciones automáticas con Pydantic
- Campos opcionales y valores por defecto
- Field y validaciones avanzadas
- Validaciones personalizadas
- Modelos de respuesta
- Métodos anidados

## 📦 Dependencias

- **FastAPI**: Framework web moderno y rápido para construir APIs
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **python-dotenv**: Carga variables de entorno desde archivo .env

## 📝 Licencia

Este proyecto es de código abierto.