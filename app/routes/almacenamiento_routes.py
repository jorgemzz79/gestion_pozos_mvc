from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.almacenamiento import Almacenamiento
from app.schemas.almacenamiento_schema import AlmacenamientoCreate, AlmacenamientoUpdate, AlmacenamientoResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=AlmacenamientoResponse)
def create_almacenamiento(almacenamiento: AlmacenamientoCreate, db: Session = Depends(get_db)):
    new_almacenamiento = Almacenamiento(**almacenamiento.dict())
    db.add(new_almacenamiento)
    db.commit()
    db.refresh(new_almacenamiento)
    return new_almacenamiento

@router.get("/", response_model=List[AlmacenamientoResponse])
def get_almacenamientos(db: Session = Depends(get_db)):
    return db.query(Almacenamiento).all()

@router.get("/{almacenamiento_id}", response_model=AlmacenamientoResponse)
def get_almacenamiento(almacenamiento_id: int, db: Session = Depends(get_db)):
    almacenamiento = db.query(Almacenamiento).filter(Almacenamiento.id == almacenamiento_id).first()
    if not almacenamiento:
        raise HTTPException(status_code=404, detail="Almacenamiento no encontrado")
    return almacenamiento

@router.put("/{almacenamiento_id}", response_model=AlmacenamientoResponse)
def update_almacenamiento(almacenamiento_id: int, almacenamiento_data: AlmacenamientoUpdate, db: Session = Depends(get_db)):
    almacenamiento = db.query(Almacenamiento).filter(Almacenamiento.id == almacenamiento_id).first()
    if not almacenamiento:
        raise HTTPException(status_code=404, detail="Almacenamiento no encontrado")
    
    for key, value in almacenamiento_data.dict(exclude_unset=True).items():
        setattr(almacenamiento, key, value)
    
    db.commit()
    db.refresh(almacenamiento)
    return almacenamiento

@router.delete("/{almacenamiento_id}")
def delete_almacenamiento(almacenamiento_id: int, db: Session = Depends(get_db)):
    almacenamiento = db.query(Almacenamiento).filter(Almacenamiento.id == almacenamiento_id).first()
    if not almacenamiento:
        raise HTTPException(status_code=404, detail="Almacenamiento no encontrado")
    
    db.delete(almacenamiento)
    db.commit()
    return {"message": "Almacenamiento eliminado exitosamente"}
