from fastapi import FastAPI
from app.config.database import engine, Base
from app.routes.routes import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.routes import archivos
from app.routes.archivo_viewer import router as archivo_viewer_router


# Crear la base de datos y las tablas
Base.metadata.create_all(bind=engine)

# Inicializar FastAPI
app = FastAPI(title="Gestión de Pozos API", version="1.0.0")

#SUBIR ARCHIVOS 
app.include_router(archivos.router, prefix="/archivos", tags=["Archivos"])

app.include_router(archivo_viewer_router, prefix="/archivos", tags=["Archivos"])


# Permitir al frontend Angular comunicarse
#origins = [
#    "http://localhost:4200",  # Angular
#    "http://127.0.0.1:4200",  # por si usas IP
#    "http://172.16.3.115:4200"  # <-- agrega esta línea
#]

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # puedes usar ["*"] para permitir todo en desarrollo
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Incluir las rutas
app.include_router(api_router)












