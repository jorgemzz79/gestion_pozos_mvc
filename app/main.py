from fastapi import FastAPI
from app.config.database import engine, Base
from app.routes.routes import api_router
from fastapi.middleware.cors import CORSMiddleware

# Crear la base de datos y las tablas
Base.metadata.create_all(bind=engine)

# Inicializar FastAPI
app = FastAPI(title="Gestión de Pozos API", version="1.0.0")


# Permitir al frontend Angular comunicarse
origins = [
    "http://localhost:4200",  # Angular
    "http://127.0.0.1:4200",  # por si usas IP
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # puedes usar ["*"] para permitir todo en desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Incluir las rutas
app.include_router(api_router)








