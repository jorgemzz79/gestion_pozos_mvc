from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.models.archivo import Archivo
from app.schemas.archivo_schema import ArchivoCreate, ArchivoUpdate, ArchivoResponse
from app.auth.dependencies import get_current_user  # ✅ agregado
from app.models.usuario import Usuario              # ✅ agregado

router = APIRouter()

@router.post("/", response_model=ArchivoResponse)
def create_archivo(
    archivo: ArchivoCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    new_archivo = Archivo(**archivo.dict())
    db.add(new_archivo)
    db.commit()
    db.refresh(new_archivo)
    return new_archivo

@router.get("/", response_model=List[ArchivoResponse])
def get_archivos(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    return db.query(Archivo).all()

@router.get("/{archivo_id}", response_model=ArchivoResponse)
def get_archivo(
    archivo_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    archivo = db.query(Archivo).filter(Archivo.id == archivo_id).first()
    if not archivo:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return archivo

@router.put("/{archivo_id}", response_model=ArchivoResponse)
def update_archivo(
    archivo_id: int,
    archivo_data: ArchivoUpdate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    archivo = db.query(Archivo).filter(Archivo.id == archivo_id).first()
    if not archivo:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    
    for key, value in archivo_data.dict(exclude_unset=True).items():
        setattr(archivo, key, value)
    
    db.commit()
    db.refresh(archivo)
    return archivo

@router.delete("/{archivo_id}")
def delete_archivo(
    archivo_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)  # ✅ agregado
):
    archivo = db.query(Archivo).filter(Archivo.id == archivo_id).first()
    if not archivo:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    
    db.delete(archivo)
    db.commit()
    return {"message": "Archivo eliminado exitosamente"}
