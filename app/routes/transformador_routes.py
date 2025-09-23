from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.models.transformador import Transformador
from app.schemas.transformador_schema import TransformadorCreate, TransformadorUpdate, TransformadorResponse
from app.auth.dependencies import get_current_user
from app.models.usuario import Usuario

router = APIRouter()

@router.post("/", response_model=TransformadorResponse)
def create_transformador(
    transformador: TransformadorCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    new_transformador = Transformador(**transformador.dict())
    db.add(new_transformador)
    db.commit()
    db.refresh(new_transformador)
    return new_transformador

@router.get("/", response_model=List[TransformadorResponse])
def get_transformadores(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    return db.query(Transformador).all()

@router.get("/pozo/{pozo_id}", response_model=List[TransformadorResponse])
def get_transformadores_por_pozo(
    pozo_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    transformadores = db.query(Transformador).filter(Transformador.pozo_id == pozo_id).all()
    if not transformadores:
        raise HTTPException(status_code=404, detail="No se encontraron transformadores para este pozo")
    return transformadores

@router.get("/{transformador_id}", response_model=TransformadorResponse)
def get_transformador(
    transformador_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    transformador = db.query(Transformador).filter(Transformador.id == transformador_id).first()
    if not transformador:
        raise HTTPException(status_code=404, detail="Transformador no encontrado")
    return transformador

@router.put("/{transformador_id}", response_model=TransformadorResponse)
def update_transformador(
    transformador_id: int,
    transformador_data: TransformadorUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    transformador = db.query(Transformador).filter(Transformador.id == transformador_id).first()
    if not transformador:
        raise HTTPException(status_code=404, detail="Transformador no encontrado")
    
    for key, value in transformador_data.dict(exclude_unset=True).items():
        setattr(transformador, key, value)
    
    db.commit()
    db.refresh(transformador)
    return transformador

@router.delete("/{transformador_id}")
def delete_transformador(
    transformador_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    transformador = db.query(Transformador).filter(Transformador.id == transformador_id).first()
    if not transformador:
        raise HTTPException(status_code=404, detail="Transformador no encontrado")
    
    db.delete(transformador)
    db.commit()
    return {"message": "Transformador eliminado exitosamente"}
