from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.transformador import Transformador
from app.schemas.transformador_schema import TransformadorCreate, TransformadorUpdate, TransformadorResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=TransformadorResponse)
def create_transformador(transformador: TransformadorCreate, db: Session = Depends(get_db)):
    new_transformador = Transformador(**transformador.dict())
    db.add(new_transformador)
    db.commit()
    db.refresh(new_transformador)
    return new_transformador

@router.get("/", response_model=List[TransformadorResponse])
def get_transformadores(db: Session = Depends(get_db)):
    return db.query(Transformador).all()

@router.get("/{transformador_id}", response_model=TransformadorResponse)
def get_transformador(transformador_id: int, db: Session = Depends(get_db)):
    transformador = db.query(Transformador).filter(Transformador.id == transformador_id).first()
    if not transformador:
        raise HTTPException(status_code=404, detail="Transformador no encontrado")
    return transformador

@router.put("/{transformador_id}", response_model=TransformadorResponse)
def update_transformador(transformador_id: int, transformador_data: TransformadorUpdate, db: Session = Depends(get_db)):
    transformador = db.query(Transformador).filter(Transformador.id == transformador_id).first()
    if not transformador:
        raise HTTPException(status_code=404, detail="Transformador no encontrado")
    
    for key, value in transformador_data.dict(exclude_unset=True).items():
        setattr(transformador, key, value)
    
    db.commit()
    db.refresh(transformador)
    return transformador

@router.delete("/{transformador_id}")
def delete_transformador(transformador_id: int, db: Session = Depends(get_db)):
    transformador = db.query(Transformador).filter(Transformador.id == transformador_id).first()
    if not transformador:
        raise HTTPException(status_code=404, detail="Transformador no encontrado")
    
    db.delete(transformador)
    db.commit()
    return {"message": "Transformador eliminado exitosamente"}
