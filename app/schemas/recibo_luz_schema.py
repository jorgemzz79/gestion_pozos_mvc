from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ReciboLuzBase(BaseModel):
    bimestre: str = Field(..., max_length=20)
    consumo_kwh: float = Field(..., ge=0)
    costo_total: float = Field(..., ge=0)
    fecha_pago: Optional[date] = None

class ReciboLuzCreate(ReciboLuzBase):
    pozo_id: int

class ReciboLuzUpdate(ReciboLuzBase):
    pass

class ReciboLuzResponse(ReciboLuzBase):
    id: int
    pozo_id: int
    class Config:
        orm_mode = True
