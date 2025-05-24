from pydantic import BaseModel, Field
from typing import Optional

class MotorBase(BaseModel):
    motor: Optional[str] = Field(None, max_length=255)
    velocidad: Optional[str] = Field(None, max_length=255)
    voltaje: Optional[str] = Field(None, max_length=255)
    corriente: Optional[str] = Field(None, max_length=255)
    marca: Optional[str] = Field(None, max_length=255)
    modelo: Optional[str] = Field(None, max_length=255)
    tipo: Optional[str] = Field(None, max_length=255)
    diametro_descarga: Optional[str] = Field(None, max_length=255)
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
