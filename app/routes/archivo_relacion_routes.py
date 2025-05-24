from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.archivo_relacion import ArchivoRelacion
from app.schemas.archivo_relacion_schema import ArchivoRelacionCreate, ArchivoRelacionUpdate, ArchivoRelacionResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=ArchivoRelacionResponse)
def create_archivo_relacion(archivo_relacion: ArchivoRelacionCreate, db: Session = Depends(get_db)):
    new_relacion = ArchivoRelacion(**archivo_relacion.dict())
    db.add(new_relacion)
    db.commit()
    db.refresh(new_relacion)
    return new_relacion

@router.get("/", response_model=List[ArchivoRelacionResponse])
def get_archivos_relaciones(db: Session = Depends(get_db)):
    return db.query(ArchivoRelacion).all()

@router.get("/{relacion_id}", response_model=ArchivoRelacionResponse)
def get_archivo_relacion(relacion_id: int, db: Session = Depends(get_db)):
    relacion = db.query(ArchivoRelacion).filter(ArchivoRelacion.id == relacion_id).first()
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación de archivo no encontrada")
    return relacion

@router.put("/{relacion_id}", response_model=ArchivoRelacionResponse)
def update_archivo_relacion(relacion_id: int, relacion_data: ArchivoRelacionUpdate, db: Session = Depends(get_db)):
    relacion = db.query(ArchivoRelacion).filter(ArchivoRelacion.id == relacion_id).first()
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación de archivo no encontrada")
    
    for key, value in relacion_data.dict(exclude_unset=True).items():
        setattr(relacion, key, value)
    
    db.commit()
    db.refresh(relacion)
    return relacion

@router.delete("/{relacion_id}")
def delete_archivo_relacion(relacion_id: int, db: Session = Depends(get_db)):
    relacion = db.query(ArchivoRelacion).filter(ArchivoRelacion.id == relacion_id).first()
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación de archivo no encontrada")
    
    db.delete(relacion)
    db.commit()
    return {"message": "Relación de archivo eliminada exitosamente"}
