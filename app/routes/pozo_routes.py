from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.models.pozo import Pozo
from app.schemas.pozo_schema import PozoCreate, PozoUpdate, PozoResponse
from app.auth.dependencies import get_current_user
from app.models.usuario import Usuario

router = APIRouter()

@router.post("/", response_model=PozoResponse)
def create_pozo(
    pozo: PozoCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    new_pozo = Pozo(**pozo.dict())
    db.add(new_pozo)
    db.commit()
    db.refresh(new_pozo)
    return new_pozo

@router.get("/", response_model=List[PozoResponse])
def get_pozos(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    return db.query(Pozo).all()

@router.get("/{pozo_id}", response_model=PozoResponse)
def get_pozo(
    pozo_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    pozo = db.query(Pozo).filter(Pozo.id == pozo_id).first()
    if not pozo:
        raise HTTPException(status_code=404, detail="Pozo no encontrado")
    return pozo

@router.put("/{pozo_id}", response_model=PozoResponse)
def update_pozo(
    pozo_id: int,
    pozo_data: PozoUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    pozo = db.query(Pozo).filter(Pozo.id == pozo_id).first()
    if not pozo:
        raise HTTPException(status_code=404, detail="Pozo no encontrado")
    
    update_data = pozo_data.dict(exclude_unset=True)
    update_data.pop("updated_at", None)   # ✅ no permitir que venga del payload
    update_data.pop("created_at", None)   # opcional, también protege created_at

    for key, value in update_data.items():
        setattr(pozo, key, value)
    
    db.commit()           # onupdate=func.now() se encarga de updated_at
    db.refresh(pozo)
    return pozo


@router.delete("/{pozo_id}")
def delete_pozo(
    pozo_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    pozo = db.query(Pozo).filter(Pozo.id == pozo_id).first()
    if not pozo:
        raise HTTPException(status_code=404, detail="Pozo no encontrado")
    
    db.delete(pozo)
    db.commit()
    return {"message": "Pozo eliminado exitosamente"}
