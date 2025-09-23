# app/schemas/unidad_schema.py
from pydantic import BaseModel

class UnidadBase(BaseModel):
    nombre: str
    abreviatura: str

class UnidadCreate(UnidadBase):
    pass

class UnidadResponse(UnidadBase):
    id: int

    class Config:
        orm_mode = True   # ✅ para Pydantic v1