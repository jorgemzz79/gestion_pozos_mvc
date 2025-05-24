from pydantic import BaseModel
from typing import Optional

class ArchivoRelacionBase(BaseModel):
    archivo_id: int
    pozo_id: Optional[int] = None
    recibo_luz_id: Optional[int] = None
    medicion_id: Optional[int] = None
    modificacion_reparacion_id: Optional[int] = None

class ArchivoRelacionCreate(ArchivoRelacionBase):
    pass

class ArchivoRelacionUpdate(ArchivoRelacionBase):
    pass

class ArchivoRelacionResponse(ArchivoRelacionBase):
    id: int
    class Config:
        orm_mode = True
