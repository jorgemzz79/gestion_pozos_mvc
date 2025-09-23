from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.config.database import get_db
from app.models.mediciones import Medicion
from app.schemas import medicion_schema as schemas  # Asegúrate que esto esté bien referenciado
from app.schemas.medicion_schema import MedicionCreate, MedicionUpdate, MedicionResponse
from app.auth.dependencies import get_current_user  # ✅ agregado
from app.models.usuario import Usuario              # ✅ agregado

router = APIRouter()

@router.post("/pozos/{pozo_id}/mediciones", response_model=MedicionResponse)
def crear_medicion_para_pozo(
    pozo_id: int,
    medicion: schemas.MedicionCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    data = medicion.dict()
    data["pozo_id"] = pozo_id
    nueva = Medicion(**data)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/pozos/{pozo_id}/mediciones", response_model=List[MedicionResponse])
def listar_mediciones_por_pozo(
    pozo_id: int,
    desde: Optional[datetime] = Query(None),
    hasta: Optional[datetime] = Query(None),
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    query = db.query(Medicion).filter(Medicion.pozo_id == pozo_id)
    if desde:
        query = query.filter(Medicion.fecha >= desde)
    if hasta:
        query = query.filter(Medicion.fecha <= hasta)
    return query.order_by(Medicion.fecha.asc()).all()

@router.get("/mediciones/{medicion_id}", response_model=MedicionResponse)
def obtener_medicion(
    medicion_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    med = db.query(Medicion).filter(Medicion.id == medicion_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medición no encontrada")
    return med

@router.put("/mediciones/{medicion_id}", response_model=MedicionResponse)
def actualizar_medicion(
    medicion_id: int,
    datos: MedicionUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    med = db.query(Medicion).filter(Medicion.id == medicion_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medición no encontrada")
    for key, value in datos.dict(exclude_unset=True).items():
        setattr(med, key, value)
    db.commit()
    db.refresh(med)
    return med

@router.delete("/mediciones/{medicion_id}")
def eliminar_medicion(
    medicion_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    med = db.query(Medicion).filter(Medicion.id == medicion_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medición no encontrada")
    db.delete(med)
    db.commit()
    return {"message": "Medición eliminada correctamente"}
