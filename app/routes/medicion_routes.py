from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.medicion import Medicion
from app.schemas.medicion_schema import MedicionCreate, MedicionUpdate, MedicionResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=MedicionResponse)
def create_medicion(medicion: MedicionCreate, db: Session = Depends(get_db)):
    new_medicion = Medicion(**medicion.dict())
    db.add(new_medicion)
    db.commit()
    db.refresh(new_medicion)
    return new_medicion

@router.get("/", response_model=List[MedicionResponse])
def get_mediciones(db: Session = Depends(get_db)):
    return db.query(Medicion).all()

@router.get("/{medicion_id}", response_model=MedicionResponse)
def get_medicion(medicion_id: int, db: Session = Depends(get_db)):
    medicion = db.query(Medicion).filter(Medicion.id == medicion_id).first()
    if not medicion:
        raise HTTPException(status_code=404, detail="Medición no encontrada")
    return medicion

@router.put("/{medicion_id}", response_model=MedicionResponse)
def update_medicion(medicion_id: int, medicion_data: MedicionUpdate, db: Session = Depends(get_db)):
    medicion = db.query(Medicion).filter(Medicion.id == medicion_id).first()
    if not medicion:
        raise HTTPException(status_code=404, detail="Medición no encontrada")
    
    for key, value in medicion_data.dict(exclude_unset=True).items():
        setattr(medicion, key, value)
    
    db.commit()
    db.refresh(medicion)
    return medicion

@router.delete("/{medicion_id}")
def delete_medicion(medicion_id: int, db: Session = Depends(get_db)):
    medicion = db.query(Medicion).filter(Medicion.id == medicion_id).first()
    if not medicion:
        raise HTTPException(status_code=404, detail="Medición no encontrada")
    
    db.delete(medicion)
    db.commit()
    return {"message": "Medición eliminada exitosamente"}
