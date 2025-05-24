from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.pozo import Pozo
from app.schemas.pozo_schema import PozoCreate, PozoUpdate, PozoResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=PozoResponse)
def create_pozo(pozo: PozoCreate, db: Session = Depends(get_db)):
    new_pozo = Pozo(**pozo.dict())
    db.add(new_pozo)
    db.commit()
    db.refresh(new_pozo)
    return new_pozo

@router.get("/", response_model=List[PozoResponse])
def get_pozos(db: Session = Depends(get_db)):
    return db.query(Pozo).all()

@router.get("/{pozo_id}", response_model=PozoResponse)
def get_pozo(pozo_id: int, db: Session = Depends(get_db)):
    pozo = db.query(Pozo).filter(Pozo.id == pozo_id).first()
    if not pozo:
        raise HTTPException(status_code=404, detail="Pozo no encontrado")
    return pozo

@router.put("/{pozo_id}", response_model=PozoResponse)
def update_pozo(pozo_id: int, pozo_data: PozoUpdate, db: Session = Depends(get_db)):
    pozo = db.query(Pozo).filter(Pozo.id == pozo_id).first()
    if not pozo:
        raise HTTPException(status_code=404, detail="Pozo no encontrado")
    
    for key, value in pozo_data.dict(exclude_unset=True).items():
        setattr(pozo, key, value)
    
    db.commit()
    db.refresh(pozo)
    return pozo

@router.delete("/{pozo_id}")
def delete_pozo(pozo_id: int, db: Session = Depends(get_db)):
    pozo = db.query(Pozo).filter(Pozo.id == pozo_id).first()
    if not pozo:
        raise HTTPException(status_code=404, detail="Pozo no encontrado")
    
    db.delete(pozo)
    db.commit()
    return {"message": "Pozo eliminado exitosamente"}
