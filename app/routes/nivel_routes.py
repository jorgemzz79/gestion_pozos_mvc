from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.models.nivel import Nivel
from app.schemas.nivel_schema import NivelCreate, NivelUpdate, NivelResponse
from app.auth.dependencies import get_current_user  # ✅ Se agregó esta línea
from app.models.usuario import Usuario              # ✅ Se agregó esta línea

router = APIRouter()

@router.post("/", response_model=NivelResponse)
def create_nivel(
    nivel: NivelCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ Se agregó este parámetro
):
    new_nivel = Nivel(**nivel.dict())
    db.add(new_nivel)
    db.commit()
    db.refresh(new_nivel)
    return new_nivel

@router.get("/", response_model=List[NivelResponse])
def get_niveles(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ Se agregó este parámetro
):
    return db.query(Nivel).all()

@router.get("/{nivel_id}", response_model=NivelResponse)
def get_nivel(
    nivel_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ Se agregó este parámetro
):
    nivel = db.query(Nivel).filter(Nivel.id == nivel_id).first()
    if not nivel:
        raise HTTPException(status_code=404, detail="Nivel no encontrado")
    return nivel

@router.put("/{nivel_id}", response_model=NivelResponse)
def update_nivel(
    nivel_id: int,
    nivel_data: NivelUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ Se agregó este parámetro
):
    nivel = db.query(Nivel).filter(Nivel.id == nivel_id).first()
    if not nivel:
        raise HTTPException(status_code=404, detail="Nivel no encontrado")
    
    for key, value in nivel_data.dict(exclude_unset=True).items():
        setattr(nivel, key, value)
    
    db.commit()
    db.refresh(nivel)
    return nivel

@router.delete("/{nivel_id}")
def delete_nivel(
    nivel_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ Se agregó este parámetro
):
    nivel = db.query(Nivel).filter(Nivel.id == nivel_id).first()
    if not nivel:
        raise HTTPException(status_code=404, detail="Nivel no encontrado")
    
    db.delete(nivel)
    db.commit()
    return {"message": "Nivel eliminado exitosamente"}
