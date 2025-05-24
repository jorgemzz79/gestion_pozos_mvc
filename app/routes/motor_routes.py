
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.motor import Motor
from app.schemas.motor_schema import MotorCreate, MotorUpdate, MotorResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=MotorResponse)
def create_motor(motor: MotorCreate, db: Session = Depends(get_db)):
    new_motor = Motor(**motor.dict())
    db.add(new_motor)
    db.commit()
    db.refresh(new_motor)
    return new_motor

@router.get("/", response_model=List[MotorResponse])
def get_motores(db: Session = Depends(get_db)):
    return db.query(Motor).all()

@router.get("/{motor_id}", response_model=MotorResponse)
def get_motor(motor_id: int, db: Session = Depends(get_db)):
    motor = db.query(Motor).filter(Motor.id == motor_id).first()
    if not motor:
        raise HTTPException(status_code=404, detail="Motor no encontrado")
    return motor

@router.put("/{motor_id}", response_model=MotorResponse)
def update_motor(motor_id: int, motor_data: MotorUpdate, db: Session = Depends(get_db)):
    motor = db.query(Motor).filter(Motor.id == motor_id).first()
    if not motor:
        raise HTTPException(status_code=404, detail="Motor no encontrado")
    
    for key, value in motor_data.dict(exclude_unset=True).items():
        setattr(motor, key, value)
    
    db.commit()
    db.refresh(motor)
    return motor

@router.delete("/{motor_id}")
def delete_motor(motor_id: int, db: Session = Depends(get_db)):
    motor = db.query(Motor).filter(Motor.id == motor_id).first()
    if not motor:
        raise HTTPException(status_code=404, detail="Motor no encontrado")
    
    db.delete(motor)
    db.commit()
    return {"message": "Motor eliminado exitosamente"}
