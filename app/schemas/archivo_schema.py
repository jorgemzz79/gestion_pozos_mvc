from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ArchivoBase(BaseModel):
    nombre_archivo: str = Field(..., max_length=255)
    tipo_archivo: Optional[str] = Field(None, max_length=50)
    ruta_archivo: str = Field(..., max_length=500)
    categoria: Optional[str] = Field(None, max_length=50)
    descripcion: Optional[str] = Field(None, max_length=500)
    fecha_subida: Optional[datetime] = None

class ArchivoCreate(ArchivoBase):
    pass

class ArchivoUpdate(ArchivoBase):
    pass

class ArchivoResponse(ArchivoBase):
    id: int
    class Config:
        orm_mode = True
