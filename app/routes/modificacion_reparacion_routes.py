from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.modificacion_reparacion import ModificacionReparacion
from app.schemas.modificacion_reparacion_schema import ModificacionReparacionCreate, ModificacionReparacionUpdate, ModificacionReparacionResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=ModificacionReparacionResponse)
def create_modificacion_reparacion(modificacion: ModificacionReparacionCreate, db: Session = Depends(get_db)):
    new_modificacion = ModificacionReparacion(**modificacion.dict())
    db.add(new_modificacion)
    db.commit()
    db.refresh(new_modificacion)
    return new_modificacion

@router.get("/", response_model=List[ModificacionReparacionResponse])
def get_modificaciones_reparaciones(db: Session = Depends(get_db)):
    return db.query(ModificacionReparacion).all()

@router.get("/{modificacion_id}", response_model=ModificacionReparacionResponse)
def get_modificacion_reparacion(modificacion_id: int, db: Session = Depends(get_db)):
    modificacion = db.query(ModificacionReparacion).filter(ModificacionReparacion.id == modificacion_id).first()
    if not modificacion:
        raise HTTPException(status_code=404, detail="Modificación o reparación no encontrada")
    return modificacion

@router.put("/{modificacion_id}", response_model=ModificacionReparacionResponse)
def update_modificacion_reparacion(modificacion_id: int, modificacion_data: ModificacionReparacionUpdate, db: Session = Depends(get_db)):
    modificacion = db.query(ModificacionReparacion).filter(ModificacionReparacion.id == modificacion_id).first()
    if not modificacion:
        raise HTTPException(status_code=404, detail="Modificación o reparación no encontrada")
    
    for key, value in modificacion_data.dict(exclude_unset=True).items():
        setattr(modificacion, key, value)
    
    db.commit()
    db.refresh(modificacion)
    return modificacion

@router.delete("/{modificacion_id}")
def delete_modificacion_reparacion(modificacion_id: int, db: Session = Depends(get_db)):
    modificacion = db.query(ModificacionReparacion).filter(ModificacionReparacion.id == modificacion_id).first()
    if not modificacion:
        raise HTTPException(status_code=404, detail="Modificación o reparación no encontrada")
    
    db.delete(modificacion)
    db.commit()
    return {"message": "Modificación o reparación eliminada exitosamente"}
