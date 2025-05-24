
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ModificacionReparacionBase(BaseModel):
    tipo_modificacion: Optional[int] = None
    descripcion_modificacion_reparacion: Optional[str] = Field(None, max_length=500)
    fecha: Optional[datetime] = None
    responsable: Optional[str] = Field(None, max_length=255)

class ModificacionReparacionCreate(ModificacionReparacionBase):
    pozo_id: int

class ModificacionReparacionUpdate(ModificacionReparacionBase):
    pass

class ModificacionReparacionResponse(ModificacionReparacionBase):
    id: int
    pozo_id: int
    class Config:
        orm_mode = True
