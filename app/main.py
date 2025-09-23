# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import engine, Base
from app.routes.routes import api_router
from app.routes import archivos
from app.routes.archivo_viewer import router as archivo_viewer_router

# 🔐 IMPORTA EL ROUTER DE AUTH
from app.auth.auth_controller import router as auth_router

# Crear la base de datos y las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gestión de Pozos API", version="1.0.0")

# 🔐 MONTA /auth (esto expone /auth/login que Swagger usará como tokenUrl)
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

# Archivos
app.include_router(archivos.router, prefix="/archivos", tags=["Archivos"])
app.include_router(archivo_viewer_router, prefix="/archivos", tags=["Archivos"])

# CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Otros routers (si aquí dentro hay rutas protegidas ya tomarán el token)
app.include_router(api_router)


