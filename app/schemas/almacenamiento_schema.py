from pydantic import BaseModel, Field
from typing import Optional

class AlmacenamientoBase(BaseModel):
    tipo_almacenamiento: Optional[str] = Field(None, max_length=255)
    lat: Optional[str] = Field(None, max_length=255)
    lon: Optional[str] = Field(None, max_length=255)
    capacidad_m3: Optional[str] = Field(None, max_length=255)
    diametro_linea: Optional[str] = Field(None, max_length=255)

class AlmacenamientoCreate(AlmacenamientoBase):
    pozo_id: int

class AlmacenamientoUpdate(AlmacenamientoBase):
    pass

class AlmacenamientoResponse(AlmacenamientoBase):
    id: int
    pozo_id: int
    class Config:
        orm_mode = True
