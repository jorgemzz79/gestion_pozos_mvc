from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.nivel import Nivel
from app.schemas.nivel_schema import NivelCreate, NivelUpdate, NivelResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=NivelResponse)
def create_nivel(nivel: NivelCreate, db: Session = Depends(get_db)):
    new_nivel = Nivel(**nivel.dict())
    db.add(new_nivel)
    db.commit()
    db.refresh(new_nivel)
    return new_nivel

@router.get("/", response_model=List[NivelResponse])
def get_niveles(db: Session = Depends(get_db)):
    return db.query(Nivel).all()

@router.get("/{nivel_id}", response_model=NivelResponse)
def get_nivel(nivel_id: int, db: Session = Depends(get_db)):
    nivel = db.query(Nivel).filter(Nivel.id == nivel_id).first()
    if not nivel:
        raise HTTPException(status_code=404, detail="Nivel no encontrado")
    return nivel

@router.put("/{nivel_id}", response_model=NivelResponse)
def update_nivel(nivel_id: int, nivel_data: NivelUpdate, db: Session = Depends(get_db)):
    nivel = db.query(Nivel).filter(Nivel.id == nivel_id).first()
    if not nivel:
        raise HTTPException(status_code=404, detail="Nivel no encontrado")
    
    for key, value in nivel_data.dict(exclude_unset=True).items():
        setattr(nivel, key, value)
    
    db.commit()
    db.refresh(nivel)
    return nivel

@router.delete("/{nivel_id}")
def delete_nivel(nivel_id: int, db: Session = Depends(get_db)):
    nivel = db.query(Nivel).filter(Nivel.id == nivel_id).first()
    if not nivel:
        raise HTTPException(status_code=404, detail="Nivel no encontrado")
    
    db.delete(nivel)
    db.commit()
    return {"message": "Nivel eliminado exitosamente"}
