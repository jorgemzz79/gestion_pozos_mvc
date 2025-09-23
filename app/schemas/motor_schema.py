from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

class MotorBase(BaseModel):
    motor: Optional[str] = Field(None, max_length=255)
    velocidad: Optional[Decimal] = None
    voltaje: Optional[Decimal] = None
    corriente: Optional[Decimal] = None
    marca: Optional[str] = Field(None, max_length=255)
    modelo: Optional[str] = Field(None, max_length=255)
    tipo: Optional[str] = Field(None, max_length=255)
    diametro_descarga: Optional[Decimal] = None
    estado: Optional[str] = Field("activo", pattern="^(activo|inactivo|mantenimiento)$")
    fotos: Optional[str] = Field(None, max_length=255)
    descripcion: Optional[str] = Field(None, max_length=255)

class MotorCreate(MotorBase):
    pozo_id: int

class MotorUpdate(MotorBase):
    pass

class MotorResponse(MotorBase):
    id: int
    pozo_id: int
    class Config:
        orm_mode = True
