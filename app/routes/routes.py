from fastapi import APIRouter
from app.routes import pozo_routes, motor_routes, recibo_luz_routes, medicion_routes, \
                        modificacion_reparacion_routes, nivel_routes, transformador_routes, \
                        almacenamiento_routes, archivo_routes, archivo_relacion_routes

# Crear el enrutador principal
api_router = APIRouter()

# Incluir las rutas de cada módulo
api_router.include_router(pozo_routes.router, prefix="/pozos", tags=["Pozos"])
api_router.include_router(motor_routes.router, prefix="/motores", tags=["Motores"])
api_router.include_router(recibo_luz_routes.router, prefix="/recibos_luz", tags=["Recibos de Luz"])
api_router.include_router(medicion_routes.router, prefix="/mediciones", tags=["Mediciones"])
api_router.include_router(modificacion_reparacion_routes.router, prefix="/modificaciones_reparaciones", tags=["Modificaciones y Reparaciones"])
api_router.include_router(nivel_routes.router, prefix="/niveles", tags=["Niveles"])
api_router.include_router(transformador_routes.router, prefix="/transformadores", tags=["Transformadores"])
api_router.include_router(almacenamiento_routes.router, prefix="/almacenamiento", tags=["Almacenamiento"])
api_router.include_router(archivo_routes.router, prefix="/archivos", tags=["Archivos"])
api_router.include_router(archivo_relacion_routes.router, prefix="/archivos_relaciones", tags=["Relaciones de Archivos"])
