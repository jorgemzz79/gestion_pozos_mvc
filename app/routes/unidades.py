from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.models.unidad import Unidad
from app.schemas.unidad_schema import UnidadCreate, UnidadResponse
from app.auth.dependencies import get_current_user
from app.models.usuario import Usuario

router = APIRouter()

@router.post("/", response_model=UnidadResponse)
def crear_unidad(
    unidad: UnidadCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    nueva = Unidad(**unidad.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/", response_model=List[UnidadResponse])
def listar_unidades(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    return db.query(Unidad).order_by(Unidad.nombre).all()

@router.get("/{unidad_id}", response_model=UnidadResponse)
def obtener_unidad(
    unidad_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    unidad = db.query(Unidad).filter(Unidad.id == unidad_id).first()
    if not unidad:
        raise HTTPException(status_code=404, detail="Unidad no encontrada")
    return unidad
