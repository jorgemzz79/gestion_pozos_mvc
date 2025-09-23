from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.config.database import get_db
from app.models.motor import Motor
from app.schemas.motor_schema import MotorCreate, MotorUpdate, MotorResponse
from app.auth.dependencies import get_current_user  # ✅ agregado
from app.models.usuario import Usuario              # ✅ agregado

router = APIRouter()

@router.post("/", response_model=MotorResponse)
def create_motor(
    motor: MotorCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    new_motor = Motor(**motor.dict())
    db.add(new_motor)
    db.commit()
    db.refresh(new_motor)
    return new_motor

@router.get("/", response_model=List[MotorResponse])
def get_motores(
    pozo_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    if pozo_id is not None:
        return db.query(Motor).filter(Motor.pozo_id == pozo_id).all()
    return db.query(Motor).all()

@router.get("/pozo/{pozo_id}", response_model=List[MotorResponse])
def get_motores_por_pozo(
    pozo_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    motores = db.query(Motor).filter(Motor.pozo_id == pozo_id).all()
    if not motores:
        raise HTTPException(status_code=404, detail="No se encontraron motores para este pozo")
    return motores

@router.get("/{motor_id}", response_model=MotorResponse)
def get_motor(
    motor_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    motor = db.query(Motor).filter(Motor.id == motor_id).first()
    if not motor:
        raise HTTPException(status_code=404, detail="Motor no encontrado")
    return motor

@router.put("/{motor_id}", response_model=MotorResponse)
def update_motor(
    motor_id: int,
    motor_data: MotorUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    motor = db.query(Motor).filter(Motor.id == motor_id).first()
    if not motor:
        raise HTTPException(status_code=404, detail="Motor no encontrado")
    
    for key, value in motor_data.dict(exclude_unset=True).items():
        setattr(motor, key, value)

    db.commit()
    db.refresh(motor)
    return motor

@router.delete("/{motor_id}")
def delete_motor(
    motor_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    motor = db.query(Motor).filter(Motor.id == motor_id).first()
    if not motor:
        raise HTTPException(status_code=404, detail="Motor no encontrado")

    db.delete(motor)
    db.commit()
    return {"message": "Motor eliminado exitosamente"}
