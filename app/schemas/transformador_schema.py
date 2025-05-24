from pydantic import BaseModel, Field
from typing import Optional

class TransformadorBase(BaseModel):
    ubicacion: Optional[str] = Field(None, max_length=255)
    kva: Optional[int] = None
    voltage_primario: Optional[float] = None
    voltage_secundario: Optional[str] = Field(None, max_length=20)
    marca: Optional[str] = Field(None, max_length=50)
    serie: Optional[str] = Field(None, max_length=50)
    bomba: Optional[str] = Field(None, max_length=50)
    modelo: Optional[str] = Field(None, max_length=50)
    serie_bomba: Optional[str] = Field(None, max_length=50)

class TransformadorCreate(TransformadorBase):
    pozo_id: int

class TransformadorUpdate(TransformadorBase):
    pass

class TransformadorResponse(TransformadorBase):
    id: int
    pozo_id: int
    class Config:
        orm_mode = True
