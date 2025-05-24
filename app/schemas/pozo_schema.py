from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class PozoBase(BaseModel):
    nombre_pozo: str = Field(..., max_length=100)
    comunidad: Optional[str] = Field(None, max_length=100)
    fecha_perforacion: Optional[date] = None
    domicilio: Optional[str] = Field(None, max_length=200)
    latitud: Optional[float] = None
    longitud: Optional[float] = None
    altitud: Optional[int] = None
    profundidad: Optional[float] = None
    gasto_actual_id: Optional[int] = None
    diametro_ademe: Optional[str] = Field(None, max_length=255)
    longitud_ademe_ciego: Optional[str] = Field(None, max_length=255)
    longitud_ademe_ranurado: Optional[str] = Field(None, max_length=255)
    tren_descarga: Optional[str] = Field(None, max_length=255)
    concesion: Optional[str] = Field(None, max_length=255)

class PozoCreate(PozoBase):
    pass

class PozoUpdate(PozoBase):
    pass

class PozoResponse(PozoBase):
    id: int