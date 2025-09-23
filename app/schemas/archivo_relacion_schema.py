from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ArchivoRelacionBase(BaseModel):
    archivo_id: int
    pozo_id: Optional[int] = None
    recibo_luz_id: Optional[int] = None
    medicion_id: Optional[int] = None
    modificacion_reparacion_id: Optional[int] = None

class ArchivoRelacionCreate(ArchivoRelacionBase):
    pass

class ArchivoRelacionUpdate(ArchivoRelacionBase):
    pass

class ArchivoRelacionResponse(ArchivoRelacionBase):
    id: int
    class Config:
        orm_mode = True

# 👇 NUEVO: lo que devuelve el GET con datos del archivo + id de la relación
class ArchivoConRelacionResponse(BaseModel):
    relacion_id: int
    id: int                       # id del archivo
    nombre_archivo: str
    tipo_archivo: str
    ruta_archivo: str
    categoria: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_subida: datetime

    class Config:
        orm_mode = True
