from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CatalogoModRepBase(BaseModel):
    nombre: str = Field(..., max_length=255)
    tipo: Optional[str] = Field(None, max_length=255)
    descripcion: Optional[str] = Field(None, max_length=255)
    activo: bool = True


class CatalogoModRepResponse(CatalogoModRepBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
