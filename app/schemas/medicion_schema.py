from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MedicionBase(BaseModel):
    fecha: datetime = Field(...)
    gasto: Optional[float] = None
    acumulado: Optional[float] = None

class MedicionCreate(MedicionBase):
    pozo_id: int

class MedicionUpdate(MedicionBase):
    pass

class MedicionResponse(MedicionBase):
    id: int
    pozo_id: int
    class Config:
        orm_mode = True
