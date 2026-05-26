from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class EmpleadoBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    nombre: str = Field(..., min_length=1, max_length=255)
    puesto: Optional[str] = Field(None, max_length=100)
    departamento: Optional[str] = Field(None, max_length=100)
    activo: bool = True


class EmpleadoCreate(EmpleadoBase):
    pass


class EmpleadoUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    nombre: Optional[str] = Field(None, min_length=1, max_length=255)
    puesto: Optional[str] = Field(None, max_length=100)
    departamento: Optional[str] = Field(None, max_length=100)
    activo: Optional[bool] = None


class EmpleadoResponse(EmpleadoBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
