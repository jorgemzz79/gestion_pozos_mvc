from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class NivelBase(BaseModel):
    tipo_nivel: Optional[str] = Field(None, max_length=255)
    abatimiento: Optional[str] = Field(None, max_length=255)
    fecha_medicion: Optional[datetime] = None

class NivelCreate(NivelBase):
    pozo_id: int

class NivelUpdate(NivelBase):
    pass

class NivelResponse(NivelBase):
    id: int
    pozo_id: int
    class Config:
        orm_mode = True
