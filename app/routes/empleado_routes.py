from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List

from app.auth.dependencies import get_current_user
from app.config.database import get_db
from app.models.empleado import Empleado
from app.models.usuario import Usuario
from app.schemas.empleado_schema import EmpleadoCreate, EmpleadoResponse, EmpleadoUpdate

router = APIRouter()


@router.get("/", response_model=List[EmpleadoResponse])
def get_empleados(
    incluir_inactivos: bool = Query(False),
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user),
):
    query = db.query(Empleado)
    if not incluir_inactivos:
        query = query.filter(Empleado.activo == True)
    return query.order_by(Empleado.nombre).all()


@router.post("/", response_model=EmpleadoResponse)
def create_empleado(
    empleado: EmpleadoCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user),
):
    new_empleado = Empleado(**empleado.model_dump())
    db.add(new_empleado)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Ya existe un empleado con ese nombre")
    db.refresh(new_empleado)
    return new_empleado


@router.get("/{empleado_id}", response_model=EmpleadoResponse)
def get_empleado(
    empleado_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user),
):
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado


@router.put("/{empleado_id}", response_model=EmpleadoResponse)
def update_empleado(
    empleado_id: int,
    empleado_data: EmpleadoUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user),
):
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    for key, value in empleado_data.model_dump(exclude_unset=True).items():
        setattr(empleado, key, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Ya existe un empleado con ese nombre")
    db.refresh(empleado)
    return empleado


@router.delete("/{empleado_id}")
def delete_empleado(
    empleado_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user),
):
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    empleado.activo = False
    db.commit()
    return {"message": "Empleado dado de baja exitosamente"}
