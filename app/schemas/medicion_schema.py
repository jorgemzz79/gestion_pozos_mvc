from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MedicionBase(BaseModel):
    pozo_id: int
    tipo_medicion: str
    valor: float
    unidad_id: Optional[int]
    fecha: datetime

class MedicionCreate(MedicionBase):
    pass

class MedicionUpdate(BaseModel):
    tipo_medicion: Optional[str]
    valor: Optional[float]
    unidad_id: Optional[int]
    fecha: Optional[datetime]

class MedicionResponse(MedicionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True