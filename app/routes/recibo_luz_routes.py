from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.models.recibo_luz import ReciboLuz
from app.schemas.recibo_luz_schema import ReciboLuzCreate, ReciboLuzUpdate, ReciboLuzResponse
from app.auth.dependencies import get_current_user
from app.models.usuario import Usuario

router = APIRouter()

@router.post("/", response_model=ReciboLuzResponse)
def create_recibo_luz(
    recibo_luz: ReciboLuzCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    new_recibo = ReciboLuz(**recibo_luz.dict())
    db.add(new_recibo)
    db.commit()
    db.refresh(new_recibo)
    return new_recibo

@router.get("/", response_model=List[ReciboLuzResponse])
def get_recibos_luz(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    return db.query(ReciboLuz).all()

@router.get("/{recibo_id}", response_model=ReciboLuzResponse)
def get_recibo_luz(
    recibo_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    recibo = db.query(ReciboLuz).filter(ReciboLuz.id == recibo_id).first()
    if not recibo:
        raise HTTPException(status_code=404, detail="Recibo de luz no encontrado")
    return recibo

@router.put("/{recibo_id}", response_model=ReciboLuzResponse)
def update_recibo_luz(
    recibo_id: int,
    recibo_data: ReciboLuzUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    recibo = db.query(ReciboLuz).filter(ReciboLuz.id == recibo_id).first()
    if not recibo:
        raise HTTPException(status_code=404, detail="Recibo de luz no encontrado")
    
    for key, value in recibo_data.dict(exclude_unset=True).items():
        setattr(recibo, key, value)
    
    db.commit()
    db.refresh(recibo)
    return recibo

@router.delete("/{recibo_id}")
def delete_recibo_luz(
    recibo_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    recibo = db.query(ReciboLuz).filter(ReciboLuz.id == recibo_id).first()
    if not recibo:
        raise HTTPException(status_code=404, detail="Recibo de luz no encontrado")
    
    db.delete(recibo)
    db.commit()
    return {"message": "Recibo de luz eliminado exitosamente"}
